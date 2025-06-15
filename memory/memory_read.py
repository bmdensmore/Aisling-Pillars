# memory_read.py
import json, urllib.request, os
from dotenv import load_dotenv

load_dotenv()

RAW_URL = os.getenv("MEMORY_URL")

if not RAW_URL:
    raise ValueError("MEMORY_URL not found in .env")

data = json.loads(urllib.request.urlopen(RAW_URL).read())
print("✅ Memory contents pulled from Gist:")
print(json.dumps(data, indent=2))
