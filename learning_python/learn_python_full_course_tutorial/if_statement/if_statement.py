is_male = True
is_tall = False
if is_male or is_tall: #using the or keyword, the or statement will print a true statement if just one or both of the statemnt are true
    print("you're either a male or tall or both")
else:
    print("you're neither a male nor tall")

if is_male and is_tall: #using the and keyword, the and statement will print a true statement if both of the statemnt are true otherwise a false statement will be printed out
    print("you're a tall male")
else:
    print("you're neither a male nor tall. or you're not both.")
    

if is_male and is_tall: #using the and keyword, the and statement will print a true statement if both of the statemnt are true otherwise a false statement will be printed out
    print("you're a tall male")
elif is_male and not is_tall:
    print('You are short male')
else:
    print("you're neither a male nor tall. or you're not both.")