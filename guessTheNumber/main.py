import random
from art import logo


def greeting():
    print("""
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    Type 'easy' or 'hard'.
    """)
    difficulty = input('Choose a difficulty: ')
    if difficulty.lower() == 'hard':
        # number of lives
        return 5
    else:
        # number of lives
        return 10


def playGame():
    print(logo)
    lives = greeting()
    number = random.randint(0, 100)
    print(f'Lives remaining: {lives}')
    while lives:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > number:
            lives -= 1
            print("Too high.")
        elif guess < number:
            lives -= 1
            print('Too low.')
        else:
            print("You guessed the number!")
            break
    else:
        print("You lost")


playGame()
