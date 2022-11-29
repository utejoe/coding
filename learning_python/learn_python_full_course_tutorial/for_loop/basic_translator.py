#making a language from english where all vowels bcoms g 
#e.g cat = cgt, big= bgg, rat= rgt
def translate(phrase): #defining the translate function to translate a particular phrase
    translation = "" #setting the translation as an empty string
    for letter in phrase: #looping through the phrase word using the for_loop
        if letter.lower() in "aeiou": # the if statement for converting all vowel words
            if letter.isupper(): # if letter for uppercase words
                translation = translation + "G" # converting the vowel words to g
            else:
                translation = translation + "g" # if not vowel it prints the words as it is
         
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))