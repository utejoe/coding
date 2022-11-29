#limiting the amount of trials in guessing the word
secret_word = "giraffe" #the word the user is to guess correctly
guess = "" # this tells how many times the user as guessed, the variable to store the users response
guess_count = 0 #it's to 0 cos the user has not started counting
guess_limit = 3 #this variable tells us how many times the user is allowed to guess the game
out_of_guesses = False # it tells us if the user has no more guesses here it is false
print("guess the name of the animal correctly; lion, goat, fish, giraffe, dog, rat, tiger, elephant, fowl, cattle, shark, whale, eagle.\n you've 3 trials.")
while guess != secret_word and not(out_of_guesses): # the while condition if the user get it incorrectly, to make it guess it again
    if guess_count < guess_limit: # using the if statement to check if the user is out of guesses
        guess = input("Enter guess: ")
        guess_count += 1 #adding 1 to every guess the user as guessed
    else:
        out_of_guesses = True 

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win")