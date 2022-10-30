def print_total(customer_name, items):
    print("Total for {}".format(customer_name))
    total = 0
    for item in items:
       total = total + item
    print("${}".format(total))
print_total(items=[4.52, 6.31, 5.00], customer_name="Karen")
