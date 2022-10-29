numbers = [0, 2, 5, 2, 0, 20, 30, 9, 99, 100]
for number in numbers:
    if number == 0:
        print ("Ugh. You gave me a 0")
        continue
    new_number = 100.0/number
    print("100/{} = {}".format(number, new_number))
