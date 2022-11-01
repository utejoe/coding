class Test(object):
    def __init__(self, num):
        self.num = num
    def __eq__(self, other):
        if self.num == other.num:
            return True
        else:
            return False

a = Test(5)
b = Test(5)
c = Test(7)
print(a == b)
print(a==c)
