# <*********
# GLOBAL VARIABLES & IMPORTS
from art import logo
import random
# from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# ********/>

# <*********
# FUNCTIONS

# Function returns random card from deck


def draw_random_card():
    random_index = random.randint(0, len(cards) - 1)
    return cards[random_index]

# Function calculates either user's or computer's current score


def add_current_score(player_card_list):
    score = 0
    for i in range(len(player_card_list)):
        score += player_card_list[i]

    if score == 21 and len(player_card_list) == 2:
        return 0

    if 11 in player_card_list and score > 21:
        ace_card_index = player_card_list.index(11)
        player_card_list[ace_card_index] == 1
    return score


def compare_scores(user_score, comp_score):
    game_outcomes = {
        "both-over": "You have gone over 21. You lose! :p\n",
        "draw": "It's a draw :O",
        "user-blackjack": "You have won Blackjack!\n",
        "comp-blackjack": "You have lost. The computer has drawn a Blackjack.\n",
        "user-over": "You have gone over 21 and lost :(\n",
        "comp-over": "The computer has gone over 21. You won!\n",
        "user-greater": "You win against the computer!\n",
        "other": "You have lost :(\n"
    }

    if user_score > 21 and comp_score > 21:
        return game_outcomes["both-over"]

    if user_score == comp_score:
        return game_outcomes["draw"]
    elif user_score == 0:
        return game_outcomes["user-blackjack"]
    elif comp_score == 0:
        return game_outcomes["comp-blackjack"]
    elif user_score > 21:
        return game_outcomes["user-over"]
    elif comp_score > 21:
        return game_outcomes["comp-over"]
    elif user_score > comp_score:
        return game_outcomes["user-greater"]
    else:
        return game_outcomes["other"]

# Function initializes game


def game_init():
    # Variables initialized
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
            # Reset the card hands and scores after restarting game
            user_cards = []
            computer_cards = []

            user_score = 0
            computer_score = 0
            # Game started
            print(logo)

            # Two cards are drawn for each of the user and computer(dealer)
            for i in range(2):
                user_cards.append(draw_random_card())
                computer_cards.append(draw_random_card())

            # While neither the user's nor the computer's score is over 21, the game will continue until the
            # user decides to stay
            game_over = False

            while not game_over:
                user_score = add_current_score(user_cards)
                computer_score = add_current_score(computer_cards)

                print(f"Your cards: {user_cards}, current score: {user_score}")
                print(f"Computer's first card: {computer_cards[0]}")

                if user_score == 0 or computer_score == 0 or user_score == 21:
                    game_over = True
                else:
                    dealer_hit = input(
                        "Type 'y' to get another card and 'n' to stay.\n")

                    if dealer_hit == "y":
                        user_cards.append(draw_random_card())
                    elif dealer_hit == "n":
                        game_over = True

            # The computer's turn to draw cards if the count is under 17 and until the computer's card count reaches 17 or more.
            # After the count is 17 or more, the computer's card count will be calculated and both scores will be compared
            # to determine the winner
            while computer_score != 0 and computer_score < 17:
                computer_cards.append(draw_random_card())
                computer_score = add_current_score(computer_cards)

            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(
                f"Computer's final hand: {computer_cards}, final score: {computer_score}")

            print(compare_scores(user_score, computer_score))
        else:
            print("Please enter either 'y' or 'n'.\n")


# *******/>
game_init()
