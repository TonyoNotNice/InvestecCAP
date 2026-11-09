"""
add_id_to_csv.py
Adds a sequential ID column to the transactions CSV.
"""

import csv
from pathlib import Path

CAP_DATA = Path(r"C:\Users\HP\OneDrive\Desktop\sap-hana-admin-portfolio\investec-cap\db\data-backup")
OUTPUT = Path(r"C:\Users\HP\OneDrive\Desktop\sap-hana-admin-portfolio\investec-cap\db\data")
OUTPUT.mkdir(parents=True, exist_ok=True)

# Transactions - add ID
with open(CAP_DATA / "investec.monitor-Transactions.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

with open(OUTPUT / "investec.monitor-Transactions.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["ID"] + list(rows[0].keys())
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i, row in enumerate(rows, start=1):
        row["ID"] = i
        writer.writerow(row)

print(f"Wrote {len(rows)} transactions with sequential IDs")

# Accounts - fix boolean capitalization
with open(CAP_DATA / "investec.monitor-Accounts.csv", encoding="utf-8") as f:
    accounts = list(csv.DictReader(f))

for a in accounts:
    a["kycCompliant"] = a["kycCompliant"].lower()

with open(OUTPUT / "investec.monitor-Accounts.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=accounts[0].keys())
    writer.writeheader()
    writer.writerows(accounts)

print(f"Wrote {len(accounts)} accounts (booleans lowercased)")

# Balances - copy as-is
import shutil
shutil.copy(CAP_DATA / "investec.monitor-Balances.csv", OUTPUT / "investec.monitor-Balances.csv")
print("Copied balances CSV")