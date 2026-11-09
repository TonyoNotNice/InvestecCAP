"""
fetch_to_csv.py
Fetch Investec data and write CAP CSV seed files.
"""

import json
import csv
import requests
from requests.auth import HTTPBasicAuth
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("INVESTEC_CLIENT_ID")
CLIENT_SECRET = os.getenv("INVESTEC_CLIENT_SECRET")
API_KEY = os.getenv("INVESTEC_API_KEY")
BASE_URL = "https://openapisandbox.investec.com"

CAP_DATA = Path(r"C:\Users\HP\OneDrive\Desktop\sap-hana-admin-portfolio\investec-cap\db\data")
CAP_DATA.mkdir(parents=True, exist_ok=True)


def get_token():
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(
        f"{BASE_URL}/identity/v2/oauth2/token",
        headers=headers,
        data={"grant_type": "client_credentials"},
        auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
        timeout=30
    )
    response.raise_for_status()
    return response.json()["access_token"]


def get(path, token):
    return requests.get(
        f"{BASE_URL}{path}",
        headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
        timeout=30
    ).json()


def main():
    print("Fetching token...")
    token = get_token()

    print("Fetching accounts...")
    accounts = get("/za/pb/v1/accounts", token)["data"]["accounts"]
    print(f"  {len(accounts)} accounts")

    with open(CAP_DATA / "investec.monitor-Accounts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["accountId","accountNumber","accountName","referenceName",
                         "productName","kycCompliant","profileId","profileName"])
        for a in accounts:
            writer.writerow([a["accountId"], a["accountNumber"], a["accountName"],
                             a["referenceName"], a["productName"], a["kycCompliant"],
                             a["profileId"], a["profileName"]])

    all_transactions = []
    all_balances = []

    for acct in accounts:
        aid = acct["accountId"]
        name = acct["referenceName"]

        print(f"Fetching balance for {name}...")
        bal = get(f"/za/pb/v1/accounts/{aid}/balance", token)["data"]
        all_balances.append(bal)

        print(f"Fetching transactions for {name}...")
        txs = get(f"/za/pb/v1/accounts/{aid}/transactions", token)["data"]["transactions"]
        all_transactions.extend(txs)
        print(f"  {len(txs)} transactions")

    with open(CAP_DATA / "investec.monitor-Balances.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["accountId","currentBalance","availableBalance","budgetBalance",
                         "straightBalance","cashBalance","currency"])
        for b in all_balances:
            writer.writerow([b["accountId"], b["currentBalance"], b["availableBalance"],
                             b["budgetBalance"], b["straightBalance"], b["cashBalance"],
                             b["currency"]])

    with open(CAP_DATA / "investec.monitor-Transactions.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["uuid","accountId","txType","transactionType","status",
                         "description","cardNumber","postedOrder","postingDate",
                         "valueDate","actionDate","transactionDate","amount","runningBalance"])
        for t in all_transactions:
            writer.writerow([t["uuid"], t["accountId"], t["type"], t["transactionType"],
                             t["status"], t["description"], t.get("cardNumber",""),
                             t["postedOrder"], t["postingDate"], t["valueDate"],
                             t["actionDate"], t["transactionDate"], t["amount"],
                             t["runningBalance"]])

    print(f"\nTotal: {len(all_balances)} balances, {len(all_transactions)} transactions")
    print(f"CSVs written to: {CAP_DATA}")


if __name__ == "__main__":
    main()