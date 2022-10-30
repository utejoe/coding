def get_total (items):
    total = 0
    for item in items:
         total = total + item 
    return total

items = [2, 5, 7, 8, 2]
items_total = get_total(items)
print(items_total)


def get_square_and_cube(number):
    square =number ** 2
    cube = number ** 3
    return square, cube

result = get_square_and_cube(5)
print(result)