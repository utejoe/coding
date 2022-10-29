while True:
    text = input("Give me some text, and I'll count the e's. Enter 'q' to quit: ")
    if text == 'q':
        break
    print (text.count('e'))