print(2**3)#normal exponential funcion in python i.e raising 2 to the power of 3

#using for loop in solving exponent
def raise_to_power(base_num, pow_num): #naming the exponent function as *raise to power*
    result = 1 #creating a variable naming/assigning it as 1
    for index in range(pow_num): #creating a for loop with a range of the pow_num, i.e if pow_num is 4 it'll loop through 4 times if 3 it"ll loop 3 times etc.
        result = result * base_num
    return result


print(raise_to_power(3,7))