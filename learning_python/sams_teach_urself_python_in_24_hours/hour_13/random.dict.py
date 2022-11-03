from random import randint
frequency = {}
for i in range(1000):
    num = randint(1, 10)
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1
print(frequency)
