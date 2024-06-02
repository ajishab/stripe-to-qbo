# stripe-to-qbo

Simple python script to convert a Transaction Summary Report csv file from Stripe to transacations CSV that can be imported to a bankfeed in QuickBooks Online.  This creates banks transactions showing deposits for the full amount of the stripe charge then a final transacation for total stripe fees. I use this monthly to import stripe transations to a Stripe account in QBO and then match them to invoices as payments.

*Usage*
python3 stripe2qbo.py stripereport.csv qbofile.csv
