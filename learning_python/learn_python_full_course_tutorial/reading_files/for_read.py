# using for loop in combination with read mode 
open("employees.txt", "r") #command to open the file, with the read mode

employee_file = open("employees.txt", "r") # saving the file into the employee_file variable
for employee in employee_file.readlines():
    print(employee)
employee_file.close()