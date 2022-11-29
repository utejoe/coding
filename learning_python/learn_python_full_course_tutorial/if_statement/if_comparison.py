def max_num(num1, num2, num3): #creating a function to determine the largest of 3 numbers
    if num1 >= num2 and num1 >= num3: # the if statement in comparing the nos
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(3, 4, 5)) #since num3 is the biggest 5 will be printed out
print(max_num(9,2,5)) #since num1 is the biggest 9 will be printed out
print(max_num(3,8,2)) #since num2 is the biggest 8 will be printed out
# it doesnt matter which of the num, it will just print the num(1,2 or 3 ) that is the biggest