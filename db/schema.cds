namespace investec.monitor;

entity Accounts {
    key accountId       : String(100);
    accountNumber       : String(50);
    accountName         : String(200);
    referenceName       : String(200);
    productName         : String(100);
    kycCompliant        : Boolean;
    profileId           : String(50);
    profileName         : String(100);
}

entity Balances {
    key accountId       : String(100);
    currentBalance      : Decimal(18,2);
    availableBalance    : Decimal(18,2);
    budgetBalance       : Decimal(18,2);
    straightBalance     : Decimal(18,2);
    cashBalance         : Decimal(18,2);
    currency            : String(10);
}

entity Transactions {
    key ID              : Integer;
    accountId           : String(100);
    uuid                : String(100);
    txType              : String(20);
    transactionType     : String(100);
    status              : String(50);
    description         : String(500);
    cardNumber          : String(50);
    postedOrder         : Integer;
    postingDate         : Date;
    valueDate           : Date;
    actionDate          : Date;
    transactionDate     : Date;
    amount              : Decimal(18,2);
    runningBalance      : Decimal(18,2);
}