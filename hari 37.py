# hari_ke_37.py
import json

data = {"nama": "Ical", "umur": 21}
json_str = json.dumps(data)
print("JSON string:", json_str)

parsed = json.loads(json_str)
print("Nama dari JSON:", parsed["nama"])
