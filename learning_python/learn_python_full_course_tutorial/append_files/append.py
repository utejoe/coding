open("employees.txt", "a") #command to open the file, with the append(a) mode

employee_file = open("employees.txt", 'a') # assigning a variable to the employee.txt file

employee_file.write("\nToby - Human Resources") # this will  add Toby - Human Resources to the 'employees.txt file... \n makes it enter the next line

employee_file.close