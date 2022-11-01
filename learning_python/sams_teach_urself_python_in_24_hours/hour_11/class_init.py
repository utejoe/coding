class Student(object):
    def __init__(self):
        self.name = "None"
        self.grade = "K"
        self.district = "Orange County"

student1 = Student()
print(student1.name)


class Student(object):
    def __init__(self, name = "None", grade = "K", district = "Orange Country"):
        self.name = name
        self.grade = grade
        self.district = district

student1 = Student()
student2 = Student(name = "Byron Blaze",
                        grade = "12",
                        district = "Fairfax County")
print(student1.name)

print(student2.name)