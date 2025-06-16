import os
import hashlib
import json
import argparse
from datetime import datetime, timezone

# --- CLI Setup ---
parser = argparse.ArgumentParser(description="Append a new hash entry from a memory snapshot.")
parser.add_argument("--file", type=str, required=True, help="Path to memory snapshot (e.g., memory_Azuric-17.json)")
parser.add_argument("--note", type=str, default="", help="Optional note to attach to the entry")
args = parser.parse_args()

SNAPSHOT_PATH = args.file
SNAPSHOTS_DIR = "snapshots"
LOG_PATH = os.path.join(SNAPSHOTS_DIR, "hash_chain.log")

# --- Ensure log directory exists ---
os.makedirs(SNAPSHOTS_DIR, exist_ok=True)

# --- Load snapshot ---
try:
    with open(SNAPSHOT_PATH, "r", encoding="utf-8") as f:
        snapshot_data = json.load(f)
except Exception as e:
    print(f"❌ Failed to load snapshot: {e}")
    exit(1)

# --- Serialize and hash the snapshot content ---
snapshot_string = json.dumps(snapshot_data, sort_keys=True).encode('utf-8')
snapshot_hash = hashlib.sha256(snapshot_string).hexdigest()

# --- Get previous chain hash from log ---
prev_hash = "0" * 64  # Genesis
if os.path.exists(LOG_PATH):
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
        if lines:
            last_line = lines[-1].strip()
            try:
                prev_hash = last_line.split(" | ")[2]
            except IndexError:
                pass

# --- Create new chain hash ---
chain_input = (prev_hash + snapshot_hash).encode('utf-8')
chain_hash = hashlib.sha256(chain_input).hexdigest()

# --- Timestamp ---
timestamp = datetime.now(timezone.utc).isoformat()

# --- Pull sky_marker if available ---
sky_marker = snapshot_data.get("Sky-marker", "UNKNOWN")

# --- Compose log entry ---
log_entry = f"{timestamp} | Sky-marker: {sky_marker} | {snapshot_hash} | {chain_hash} | {args.note.strip()}\n"

# --- Append to log ---
with open(LOG_PATH, "a", encoding="utf-8") as f:
    f.write(log_entry)

print(f"✅ Hash chain entry recorded for: {sky_marker}")
print(f"📝 Note: {args.note}")
