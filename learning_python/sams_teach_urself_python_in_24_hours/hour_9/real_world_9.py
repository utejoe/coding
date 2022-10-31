def get_specials():
monday = {'B': 'Horseradish omelet. Note:  better than it sounds',
          'L': 'Momma\'s Curry. Note: Can be nmade spicy.',
'D': 'Beef brisket. Note: Comes with au jus. That\'s pronounced "Oh jhoo", not "Ow Juice"'}
tuesday = {'B': 'Sausage gravy over biscuits. Note: Toast can be subbed.',
'L': 'Grilled cheese and tomato soup. Note: We have vegan cheese.',
'D': 'Meatloaf. Note: Comes with catsup on the top. Not optional.'}
wednesday = {'B': 'Horseradish omelet. Note: better than it sounds',
'L': 'Momma\'s Curry. Note: Can be made spicy.',
'D': 'Beef brisket. Note: Comes with au jus. That\'s pronounced "Oh jhoo", not "Ow Juice"'}
thursday = {'B': 'Horseradish omelet. Note: better than it sounds',
'L': 'Momma\'s Curry. Note: Can be made spicy.',
'D': 'Beef brisket. Note: Comes with au jus. That\'s pronounced "Oh jhoo", not "Ow Juice"'}
friday = {'B': 'Horseradish omelet. Note: better than it sounds',
'L': 'Momma\'s Curry. Note: Can be made spicy.',
'D': 'Beef brisket. Note: Comes with au jus. That\'s pronounced "Oh jhoo", not "Ow Juice"'}
saturday = {'B': 'Horseradish omelet. Note:better than it sounds',
'L': 'Momma\'s Curry. Note: Can be
made spicy.',
'D': 'Beef brisket. Note: Comes with
au jus. That\'s pronounced "Oh
jhoo", not "Ow Juice"'}
sunday = {'B': 'Horseradish omelet. Note:
better than it sounds',
'L': 'Momma\'s Curry. Note: Can be
made spicy.',
'D': 'Beef brisket. Note: Comes with
au jus. That\'s pronounced "Oh
jhoo", not "Ow Juice"'}
specials = {'M': monday,
'T': tuesday,
'W': wednesday,
'R': thursday,
'F': friday,
'St': saturday,
'Sn': sunday}
return specials
def print_special(special):
print "The special is:"
print special
print ""15
def get_day():
while True:
day = raw_input("Day (M/T/W/R/F/St/Sn): ")
if day.upper() in ['M', 'T', 'W', 'R', 'F',
'ST', 'SN']:
return day.upper()
else:
print "I'm sorry, but {} isn't
valid.".format(day)
def get_time():
while True:
time = raw_input("Time (B/L/D): ")
if time.upper() in ['B', 'L', 'D']:
return time.upper()
else:
print "I'm sorry, but {} isn't a valid
time.".format(time)
better than it sounds',
'L': 'Momma\'s Curry. Note: Can be
made spicy.',
'D': 'Beef brisket. Note: Comes with`
au jus. That\'s pronounced "Oh
jhoo", not "Ow Juice"'}
specials = {'M': monday,
'T': tuesday,
'W': wednesday,
'R': thursday,
'F': friday,
'St': saturday,
'Sn': sunday}
return specials
def print_special(special):
print "The special is:"
print special
print ""15
def get_day():
while True:
day = raw_input("Day (M/T/W/R/F/St/Sn): ")
if day.upper() in ['M', 'T', 'W', 'R', 'F',
'ST', 'SN']:
return day.upper()
else:
print "I'm sorry, but {} isn't
valid.".format(day)
def get_time():
while True:
time = raw_input("Time (B/L/D): ")
if time.upper() in ['B', 'L', 'D']:
return time.upper()
else:
print "I'm sorry, but {} isn't a valid
time.".format(time)
