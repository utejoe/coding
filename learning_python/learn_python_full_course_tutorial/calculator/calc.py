#in python once we input a value numbers/words it is converted into a string automatically. so we ought to convert to an integer if we want it so
num1 = float (input("Enter first number: ")) #and input command and then using the float command to convert it to a flaot
op = input("Enter operator: ") # this is the operator and we''re leaving it as a string
num2 = float (input("Enter second number: ")) #inputting the second no (num2)

if op == "+": #using the if statement to check if the operator is a +
    print(num1 + num2)
elif op == '-': #using the elseif statement
    print(num1 - num2)
elif op == "/":
    print(num1/num2)
elif op == '*':
    print(num1*num2)
else: # incase the user input any op that's not available above
    print("Invalid operator") # it'll print this if the user input and invalid op