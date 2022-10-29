age = input("Please give me your age in years (eg. 30): ")
while not age.isdigit():
    print("I'm sorry, but {} isn't valid.".format(age))
    age = input("please give me your age in years (eg. 30): ")
print("Thanks! Your age is set to {} ".format(age))
