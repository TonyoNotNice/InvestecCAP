using investec.monitor from '../db/schema';

service InvestecService {
    entity Accounts as projection on monitor.Accounts;
    entity Balances as projection on monitor.Balances;
    entity Transactions as projection on monitor.Transactions;
}