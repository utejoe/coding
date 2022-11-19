from random import randint

def main():
    print("Welcome to the number guessing game!")
    number = randint(1, 10)
    while True:
        guess = 3
        input("Guess a number between one and ten: ")
        if int(guess) == number:
            print("That's right!")
            break
        elif int(guess) > number:
            print("Sorry, that's too high. Guess again please!")
        elif int(guess) < number:
            print("Sorry, that's too low. Guess again please!")

if __name__ == '__main__':
    main()