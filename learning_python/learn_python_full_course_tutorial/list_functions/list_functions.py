lucky_numbers = [4, 8, 15, 16, 23, 42] #a list of lucky numbers
friends = ['Kelvin', "Karen", "Jim", 'Jim', "Jim", 'Oscar', "Toby"] #a list of friends
print(lucky_numbers)
print(friends)
lucky_numbers.append('jude') #using append to add an extra element
print(lucky_numbers)
friends.insert(3, 'joshua') #using insert to add a particular element at a particular index number
print(friends)
friends.remove('joshua') #using the remove command to remove a particular element from a list
print(friends)
lucky_numbers.pop() #using the pop() command to remove the last element from the list
print(lucky_numbers) 
friends.extend(lucky_numbers) #using the extend function to add the lucky.numbers to friends list
print(friends)
print(friends.index('Toby')) #using .index command to check if an element is inside a list. if not present python will print and error mssg
print(friends.count('Jim')) #using the .count command to find out how many of same number exist in a list
friends.clear() #using the clear command to empty a particular list
print(friends)