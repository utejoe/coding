#creating a list an making all the elements inside of the list list themselves
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid: #creating my first for loop
    for col in row: #creating another for loop inside the row loop
        print(col)