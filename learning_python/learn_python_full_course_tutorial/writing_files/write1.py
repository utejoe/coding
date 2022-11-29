open("employees.txt", "w") #command to open the file, with the write(w) mode

employee_file = open("employees1.txt", 'w') # assigning a variable to the employee.txt file..
#notice the employees1.txt we're basically using write mode to create a new file

employee_file.write("\nToby - Human Resources") # we're basically creating the new file employees1.txt with "\nToby - Human Resources" inside

employee_file.close()