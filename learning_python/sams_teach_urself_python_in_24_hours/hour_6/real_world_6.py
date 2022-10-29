inventory = ['butter',
        'tomato sauce',
        'green beans',
        'chicken',
        'italian herbs',
        'garlic',
        'hamburger',
        'flour',
        'eggs',
        'noodles']

print("Welcome to the Inventory program!")
item = input("What item do you wnat to check? ")
if item in inventory:
    print("Yes, we have that.")
else:
    print("no, we don't have that.")

