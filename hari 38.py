# hari_ke_38.py
import json

# Simulasi respons API
response = '{"user": "Ical", "status": "active"}'

data = json.loads(response)
print("User:", data["user"])
print("Status:", data["status"])
