# memory_write.py
import json, os, requests, datetime
from dotenv import load_dotenv

load_dotenv()

GIST_ID = os.getenv("GIST_ID")
GH_PAT = os.getenv("GH_PAT")

if not GIST_ID or not GH_PAT:
    raise ValueError("Missing GIST_ID or GH_PAT in .env")

new_payload = {
    "Sky-marker": "Azuric-17",
    "timestamp": datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z",
    "tz": "America/Chicago"
}

res = requests.patch(
    f"https://api.github.com/gists/{GIST_ID}",
    headers={"Authorization": f"token {GH_PAT}"},
    json={"files": {"memory.json": {"content": json.dumps(new_payload, indent=2)}}}
)

if res.status_code == 200:
    print("✅ Memory anchor successfully updated.")
else:
    print(f"❌ Failed to update memory. Status: {res.status_code}")
    print(res.text)
