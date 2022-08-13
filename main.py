# *********
# GLOBAL VARIABLES & IMPORTS
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# *********

# *********
# FUNCTIONS


# Function returns random card from deck
def draw_random_card():
    random_index = random.randint(0, len(cards) - 1)
    return cards[random_index]


def add_current_score(player_card_list):
    score = 0
    for card in range(len(player_card_list) - 1):
        score += card

    return score


# Function initializes game
def game_init():
    user_cards = []
    computer_cards = []

    user_score = 0
    computer_score = 0
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

            game_started = True

            while game_started:
                print("This is the first round draw")
                for i in range(2):
                    user_cards.append(draw_random_card())
                    computer_cards.append(draw_random_card())

                for i in range(len(user_cards)):
                    user_score += user_cards[i]

                for i in range(len(computer_cards)):
                    computer_score += computer_cards[i]

                print(
                    f"    You cards: {user_cards}, current score: {user_score}"
                )
                print(
                    f"    Computer's first card: {computer_cards[0]}, computer score: {computer_score}, comp cards: {computer_cards} (for development purposes only)\n"
                )

                if user_score == 21:
                    game_started = False
                    print(
                        f"You win with a Blackjack 😎. Your final hand: {user_cards}. Final score: {user_score}.\n"
                    )
                    print(
                        f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                elif computer_score == 21:
                    game_started = False
                    print(f"Computer wins 😭. Current score {computer_score}")
                elif user_score > 21:
                    if 11 in user_cards:
                        ace_card_index = user_cards.index(11)
                        user_cards[ace_card_index] = 11
                        for i in user_cards:
                            user_score += user_cards[i]
                        if user_score > 21:
                            print(
                                f"Your final hand: {user_cards}, final score: {user_score}.\n")
                            print(
                                f"Computer's final hand: {computer_cards}, final score: {computer_score}.\n")
                            print("You have gone over 21 and lost 😭.\n")
                        else:
                            print(f"Hello")
                    else:
                        print(
                            f"Your final hand: {user_cards}, final score: {user_score}.\n")
                        print(
                            f"Computer's final hand: {computer_cards}, final score: {computer_score}.\n")
                        print("You have gone over 21 and lost 😭.\n")
                        game_started = False
                elif computer_score > 21:
                    print(
                        f"Your final hand: {user_cards}, final score: {user_score}.\n")
                    print(
                        f"Computer's final hand: {computer_cards}, final score: {computer_score}.\n")

                else:
                    game_started = False

                # get_another_card = input(
                #     "Type 'y' to get another card, type 'n' to pass:\n"
                # )

                # print(f"Your cards: {user_cards}, current score: {user_score}")
                # print(f"Computer's first card: {computer_cards[0]}")
        else:
            print("Please enter either 'y' or 'n.\n'")


# *********

game_init()
