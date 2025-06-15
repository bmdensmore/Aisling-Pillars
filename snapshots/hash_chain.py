import os
import hashlib
import json
from datetime import datetime

# Configuration
SNAPSHOT_TEXT = {
    "event": "Memory anchor set",
    "sky_marker": "Azuric-17",
    "timestamp": datetime.utcnow().isoformat() + "Z"
}

SNAPSHOTS_DIR = "snapshots"
LOG_PATH = os.path.join(SNAPSHOTS_DIR, "hash_chain.log")

# Ensure directory exists
os.makedirs(SNAPSHOTS_DIR, exist_ok=True)

# Encode snapshot
snapshot_string = json.dumps(SNAPSHOT_TEXT, sort_keys=True).encode('utf-8')
snapshot_hash = hashlib.sha256(snapshot_string).hexdigest()

# Get previous hash from log (if any)
prev_hash = "0" * 64  # Genesis hash
if os.path.exists(LOG_PATH):
    with open(LOG_PATH, "r") as f:
        lines = f.readlines()
        if lines:
            last_line = lines[-1].strip()
            try:
                prev_hash = last_line.split(" | ")[2]
            except IndexError:
                pass

# Combine to create new chain hash
chain_input = (prev_hash + snapshot_hash).encode('utf-8')
chain_hash = hashlib.sha256(chain_input).hexdigest()

# Compose new log entry
entry = f"{datetime.utcnow().isoformat()}Z | {snapshot_hash} | {chain_hash}\n"

# Write to log
with open(LOG_PATH, "a") as f:
    f.write(entry)

print("✅ Hash chain entry recorded.")
