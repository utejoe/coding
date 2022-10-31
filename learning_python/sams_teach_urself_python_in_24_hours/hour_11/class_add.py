class MyClass(object):
    a = 5
    b= 7
    def print_a(self):
        print("Hello! Here is a: {}".format(self.a))

my_object = MyClass()
my_object.print_a()
