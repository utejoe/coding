# This entire line will not be run!
print("Hello world")

#The print statement will run, but not this!
# Getting user's name, properly formatted
while True:
    name = input("Please give me your name: ")
    # Spaces are okay, everything else is bad.
    if not name.replace(' ', '').isalpha():
        print("There's some invalid characters in your name.")
        print("sorry. Please try again.")
    else:
        break
print("Welcome, {}".format(name))
