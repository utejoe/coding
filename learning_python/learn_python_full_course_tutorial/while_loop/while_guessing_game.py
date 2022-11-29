#using a while loop to create a guessing game where the user ought to get the answer right b4 the loop is terminated
secret_word = "giraffe"
print("guess the animal's name")
guess = ""

while guess != secret_word:
    guess = input("Enter guess: ")

print("YOU win!")