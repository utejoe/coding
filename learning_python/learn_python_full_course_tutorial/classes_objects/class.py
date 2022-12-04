# importing student from  class_student (the other file)
from class_student import Student

student1 = Student('Jim', "Business", 3.1, False)

student2 = Student("Pam", "Business", 2.2, True)
print(student1.gpa)
print(student2.is_on_probation)