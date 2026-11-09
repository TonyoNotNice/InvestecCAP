using InvestecService as service from '../../srv/investec-service';
annotate service.Transactions with @(
    UI.FieldGroup #GeneratedGroup : {
        $Type : 'UI.FieldGroupType',
        Data : [
            {
                $Type : 'UI.DataField',
                Label : 'ID',
                Value : ID,
            },
            {
                $Type : 'UI.DataField',
                Label : 'accountId',
                Value : accountId,
            },
            {
                $Type : 'UI.DataField',
                Label : 'uuid',
                Value : uuid,
            },
            {
                $Type : 'UI.DataField',
                Label : 'txType',
                Value : txType,
            },
            {
                $Type : 'UI.DataField',
                Label : 'transactionType',
                Value : transactionType,
            },
            {
                $Type : 'UI.DataField',
                Label : 'status',
                Value : status,
            },
            {
                $Type : 'UI.DataField',
                Label : 'description',
                Value : description,
            },
            {
                $Type : 'UI.DataField',
                Label : 'cardNumber',
                Value : cardNumber,
            },
            {
                $Type : 'UI.DataField',
                Label : 'postedOrder',
                Value : postedOrder,
            },
            {
                $Type : 'UI.DataField',
                Label : 'postingDate',
                Value : postingDate,
            },
            {
                $Type : 'UI.DataField',
                Label : 'valueDate',
                Value : valueDate,
            },
            {
                $Type : 'UI.DataField',
                Label : 'actionDate',
                Value : actionDate,
            },
            {
                $Type : 'UI.DataField',
                Label : 'transactionDate',
                Value : transactionDate,
            },
            {
                $Type : 'UI.DataField',
                Label : 'amount',
                Value : amount,
            },
            {
                $Type : 'UI.DataField',
                Label : 'runningBalance',
                Value : runningBalance,
            },
        ],
    },
    UI.Facets : [
        {
            $Type : 'UI.ReferenceFacet',
            ID : 'GeneratedFacet1',
            Label : 'General Information',
            Target : '@UI.FieldGroup#GeneratedGroup',
        },
    ],
    UI.LineItem : [
        {
            $Type : 'UI.DataField',
            Label : 'ID',
            Value : ID,
        },
        {
            $Type : 'UI.DataField',
            Label : 'accountId',
            Value : accountId,
        },
        {
            $Type : 'UI.DataField',
            Label : 'uuid',
            Value : uuid,
        },
        {
            $Type : 'UI.DataField',
            Label : 'txType',
            Value : txType,
        },
        {
            $Type : 'UI.DataField',
            Label : 'transactionType',
            Value : transactionType,
        },
    ],
);

