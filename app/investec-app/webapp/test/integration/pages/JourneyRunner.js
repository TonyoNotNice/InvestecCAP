sap.ui.define([
    "sap/fe/test/JourneyRunner",
	"investecapp/test/integration/pages/TransactionsList.gen",
	"investecapp/test/integration/pages/TransactionsObjectPage.gen"
], function (JourneyRunner, TransactionsListGenerated, TransactionsObjectPageGenerated) {
    'use strict';

    const runner = new JourneyRunner({
        launchUrl: sap.ui.require.toUrl('investecapp') + '/test/flpSandbox.html#investecapp-tile',
        pages: {
			onTheTransactionsListGenerated: TransactionsListGenerated,
			onTheTransactionsObjectPageGenerated: TransactionsObjectPageGenerated
        },
        async: true
    });

    return runner;
});

