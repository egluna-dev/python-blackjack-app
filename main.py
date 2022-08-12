# <*********
# GLOBAL VARIABLES & IMPORTS
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []

user_score = 0
computer_score = 0

# *********/>

# <*********
# FUNCTIONS


# Function returns random card from deck
def draw_random_card():
    random_index = random.randint(0, len(cards) - 1)
    return cards[random_index]


# Function initializes game
def game_init():
    program_on = True

    while program_on:
        start_game = input(
            "Do you want to play a game of Blackjack? Type 'y' if yes and 'n' if no:\n"
        )

        if start_game == 'n':
            program_on = False
            print("Good bye")
        elif start_game == 'y':

            print(logo)

            for i in range(2):
                user_cards.append(draw_random_card())
                computer_cards.append(draw_random_card())

            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(
                f"Computer's first card: {computer_cards[0]}, current score: {user_score}"
            )


# ********/>

game_init()
