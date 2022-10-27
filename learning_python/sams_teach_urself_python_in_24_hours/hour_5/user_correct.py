year = input("What year were you born [eg: 1980]? ")
if len(year) !=4 or not year.isdigit():
    print("I'm sorry, I don't like that number.")
else:
    print("That's good. Moving on!")
