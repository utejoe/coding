cart = [20.25, 30.04, 102.4, 50, 80]
for item in cart:
    print(item)
    if item > 100:
        print("You are going to require insurance on this order.")
        break

cart = [50.25, 20.98, 99.99, 1.24, .84, 60.03]
for item in cart:
    print(item)
    if item > 100:
        print("You are going to require insuirance on this order.")
        break
    else:
       print("No insurance will be required for this order.")
