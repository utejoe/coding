open("employees.txt", "r") #command to open the file, with the read mode

employee_file = open("employees.txt", "r") # saving the file into the employee_file variable

print(employee_file.readable()) #checking if the employee file is readable. if the mode is write it will print False

print(employee_file.read()) #it's basically the command to read the file

employee_file.close() #using the command close() to close the file
