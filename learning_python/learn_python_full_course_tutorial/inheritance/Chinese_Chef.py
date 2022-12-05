from class_chef import Chef

#inherting the class Chef into the ChineseChef
class ChineseChef(Chef):

    def make_special_dish(self): #overidding the make special dish function from the chef class
        print('The chef makes orange chicken')
    #the chinese chef can also do other stuffs so we add them

    def make_fried_rice(self):
        print("The chef makes fried rice")