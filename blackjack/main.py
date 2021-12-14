import random
from replit import clear
from art import logo


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards: list) -> int:
    """takes a list of cards and returns the calculated score
    :rtype: int
    """

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return int(sum(cards))


def compare(score_user: int, score_computer: int) -> str:
    if score_user == score_computer:
        return "Draw."
    elif score_computer == 0:
        return "You Lose. opponent has Blackjack!"
    elif score_user == 0:
        return "You win with a Blackjack!"
    elif score_user > 21:
        return "You went over. You Lose."
    elif score_computer > 21:
        return "Opponent went over. You win."
    elif score_user > score_computer:
        return "You win."
    else:
        return "You lose."


def play_game():
    logo()
    user_cards = []
    user_score = 0

    computer_cards = []
    computer_score = 0
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Your cards: {user_cards}, current score: {user_score}')
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("\nType 'y' to get another card, type 'n to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_cards != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("\n\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
