from Day14_art import logo, vs
from Day14_data import data

import random
# Data is an Array of Dictionaries. Each Dictionary has 4 components: Name, Follower Count (millions), Description, Country

def construct_string(first, data):
    print_string = "Compare A: "
    if not first:
        print_string = "Against B: "
    print_string += f"{data['name']}, {data['description']}, from {data['country']}"
    print(print_string)

def play_game(a):
    correct_guesses = 0
    end_game = False

    while not end_game:

        if len(data) == 0:
            return correct_guesses, 0

        a_followers = 0
        b_followers = 0

        # Print Logo
        print(logo)

        if correct_guesses > 0:
            print(f"You're right! Current score: {correct_guesses}")

        # Print A
        ## Random choice from the List of Data
        ## Generate a string
        a_followers = a["follower_count"]
        construct_string(True, a)

        # Print VS
        print(vs)

        # Print B
        ## Random choice from List of Data (NOT the same as A though)
        index = random.randint(0, len(data)-1)
        b = data.pop(index)
        b_followers = b["follower_count"]
        construct_string(False, b)

        # Obtain Input on choice
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        # Decide if decision is correct
        if choice == "a" and a_followers > b_followers or choice == "b" and b_followers > a_followers:
            # increment score
            correct_guesses += 1
            # If Correct B becomes A and we start from the top
            a = b
        else:
            # If Failed game ends and we show the number of correct guesses
            end_game = True
    return correct_guesses, -1

index = random.randint(0, len(data)-1)
a = data.pop(index)
correct_guesses, end_game_condition = play_game(a)

# If Failed game ends and we show the number of correct guesses
print(logo)
if end_game_condition == -1:
    print(f"There are no more guesses to make. Final score: {correct_guesses}")
else:
    print(f"Sorry that's wrong. Final score: {correct_guesses}")