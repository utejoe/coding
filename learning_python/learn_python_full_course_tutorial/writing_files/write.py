# this is a write file the difference between a write file and an append file is that append adds to the existing file.. while write deletes the previous works and writes new items inside the file
open("employees.txt", "w") #command to open the file, with the write(w) mode

employee_file = open("employees.txt", 'w') # assigning a variable to the employee.txt file

employee_file.write("\nKelly - Customer Service") # since we use the write mode all the file in the employee txt will be replace my kelly - Customer..... check employee_original.txt for original text

employee_file.close()