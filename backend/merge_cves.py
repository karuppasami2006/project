import json
import os

db_path = r'c:\Users\mrabi\OneDrive\Desktop\Hackathon\Hackathon\backend\cve_database.json'
new_path = r'c:\Users\mrabi\OneDrive\Desktop\Hackathon\Hackathon\backend\new_cves.json'

with open(db_path, 'r') as f:
    db = json.load(f)

with open(new_path, 'r') as f:
    new_data = json.load(f)

db.extend(new_data)

with open(db_path, 'w') as f:
    json.dump(db, f, indent=2)

print(f"Added {len(new_data)} CVEs. New total: {len(db)}")
