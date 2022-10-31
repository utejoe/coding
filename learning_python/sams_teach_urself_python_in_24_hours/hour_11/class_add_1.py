class School(object):
    name = ''
    address = ''
    type = 'grade school'
    def print_school(self):
        print(self.name)
        print(self.address)
        print("Type: " + self.type)
school1 = School()
school2 = School()
school1.name = "Wyland Elementary"
school1.address = "100 Peachtree Ave\nAtlanta GA"
school2.name = "George Mason Univevrsity"
school2.address = "300 University Way\nFairfax VA"
school2.type = "university"
print(school1.print_school())
print(school2.print_school())