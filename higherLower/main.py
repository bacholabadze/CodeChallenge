import random
from replit import clear
from art import logo, vs
from data import data

used = []


def random_person():
    person = random.choice(data)

    while person['name'] in used:
        person = random.choice(data)

    if person['name'] not in used:
        used.append(person['name'])
        return person


def more_followers(a, b):
    if a['follower_count'] > b['follower_count']:
        return 'a'
    else:
        return 'b'


def playGame():
    score = 0
    is_game_over = False

    while not is_game_over:
        clear()
        print(logo)
        if score:
            print(f"You're right! Current score:{score}")

        person_a = random_person()
        person_b = random_person()

        print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
        print(vs)
        print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")

        answer = more_followers(person_a, person_b)
        guess = input("Who has more followers? Type 'A' or 'B': ")

        if guess.lower() == answer:
            score += 1
        else:
            is_game_over = True

    print(f"Sorry, that's wrong. Final score: {score}")


playGame()
