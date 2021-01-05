# Number guessing game

from Day11_flying_solo_art import logo
import random

EASY_NO_TURNS = 10
HARD_NO_TURNS = 5

def setdificulty():
    difficulty = ""
    while "easy" not in difficulty and "hard" not in difficulty:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "hard":
        return HARD_NO_TURNS
    else:
        return EASY_NO_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_guess = random.randint(1, 100)
    print(f"Psssssst, the correct answer is {number_guess}")

    attempts = setdificulty()

    found_number = False
    while attempts > 0 and found_number is not True:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess_attempt = int(input("Make a guess: "))
        if guess_attempt == number_guess:
            found_number = True
        else:
            if guess_attempt > number_guess:
                print("Too high.")
            else:
                print("Too low.")
            
            attempts -= 1

            if attempts > 0:
                print("Guess again.")        

    if found_number == True:
        print(f"You got it! The answer was {number_guess}")
    else:
        print(f"You've run out of guesses, you lose. The number I was thinking of was {number_guess}")

game()