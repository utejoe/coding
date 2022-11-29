#creating a dictionary called monthConversions
#converting the month names to 3 letter words
#where the 3 letter words are the keys
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    "0": "January-February",
    "1": "love"
}

print(monthConversions["Nov"]) #accessing the dictionary and priting out november using the key Nov

print(monthConversions.get("Dec")) #another way of accessing the dictionary
print(monthConversions['1']) #printing out the integer keyword