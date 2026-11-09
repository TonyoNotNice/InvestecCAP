"""
convert_to_csv.py
Convert Investec JSON responses to CAP CSV import format.
"""

import json
import csv
from pathlib import Path

EVIDENCE = Path("investec-integration-portfolio/evidence/raw-responses")
CAP_DATA = Path("investec-cap/db/data")
CAP_DATA.mkdir(parents=True, exist_ok=True)

# Convert accounts
with open(EVIDENCE / "accounts.json", encoding="utf-8") as f:
    accounts = json.load(f)["data"]["accounts"]

with open(CAP_DATA / "investec.monitor-Accounts.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["accountId","accountNumber","accountName","referenceName",
                     "productName","kycCompliant","profileId","profileName"])
    for a in accounts:
        writer.writerow([a["accountId"], a["accountNumber"], a["accountName"],
                         a["referenceName"], a["productName"], a["kycCompliant"],
                         a["profileId"], a["profileName"]])

print(f"Wrote {len(accounts)} accounts")

# Convert transactions
transactions_file = next(EVIDENCE.glob("transactions-*.json"))
with open(transactions_file, encoding="utf-8") as f:
    transactions = json.load(f)["data"]["transactions"]

with open(CAP_DATA / "investec.monitor-Transactions.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["uuid","accountId","txType","transactionType","status",
                     "description","cardNumber","postedOrder","postingDate",
                     "valueDate","actionDate","transactionDate","amount","runningBalance"])
    for t in transactions:
        writer.writerow([t["uuid"], t["accountId"], t["type"], t["transactionType"],
                         t["status"], t["description"], t.get("cardNumber",""),
                         t["postedOrder"], t["postingDate"], t["valueDate"],
                         t["actionDate"], t["transactionDate"], t["amount"],
                         t["runningBalance"]])

print(f"Wrote {len(transactions)} transactions")