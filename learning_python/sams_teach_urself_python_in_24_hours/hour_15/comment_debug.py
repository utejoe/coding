from AccountingHelper import Transactions

recent = Transactions(company="WidgetCorp", type="debits")
for item in recent:
    print("Item: {}".format(item.title))
    print("Amount: (${})".format(item.amount))
    print("Note: {}".format(item.note))
    print("Card used; {}".format(item.card))
