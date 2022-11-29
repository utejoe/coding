open("employees.txt", "r") #command to open the file, with the read mode

employee_file = open("employees.txt", "r") # saving the file into the employee_file variable

print(employee_file.readable()) #checking if the employee file is readable. if the mode is write it will print False

print(employee_file.readline()) # printing out the first line in the code. and gives a space below
print(employee_file.readline()) # it prints the next line. and so on if the command is continously imputed 

print(employee_file.readlines()) # it converts all the lines of the code into an array

print(employee_file.read()) #it's basically the command to read the file

employee_file.close() #using the command close() to close the file

#some command can't function together so i created another read1.py file for more understanding
# like the read() command cant function with readline(s)() command 