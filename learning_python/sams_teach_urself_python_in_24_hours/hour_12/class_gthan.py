class Test(object):
    def __init__(self, num):
        self.num = num
    def __gte__(self, other):
        if self.num >= other.num:
            return True
        else:
            return False

alpha = Test(5)
beta = Test(5)
gamma = Test(6)
print(alpha >= beta)
print(alpha >= gamma)
print(gamma >= alpha)
