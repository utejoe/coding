try: # the try command to test error in our code. an except command should follow after
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError: #the except statement for error of 10/0 saving it as a variable err
    print("Divided by zero")
except ValueError: # using the except command to print out a statement if there's an error
    print("Invalid input") # if there's and error this statement will be print out