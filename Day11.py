# ############## Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# ############## Our Blackjack House Rules #####################

# # The deck is unlimited in size. 
# # There are no jokers. 
# # The Jack/Queen/King all count as 10.
# # The the Ace can count as 11 or 1.
# # Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# # The cards in the list have equal probability of being drawn.
# # Cards are not removed from the deck as they are drawn.
# # The computer is the dealer.

# #################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input 
# and returns the score. 
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import random


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Returns the sum of the list. However if we have 2 cards and they make 21, it returns 0"""
    # Player has a perfect Black Jack (2 cards 11 + 10)
    if len(cards) == 2 and sum(cards) == 21:
        return 0

    # Do we need to replace an 11 for a 1 if over 21?
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(p_score, d_score):
    if p_score == 0:
        print("You won! You got Blackjack!")
        return
    if d_score == 0:
        print("You loose! Computer has Blackjack")
        return
    if p_score == d_score:
        print("Its a Draw!")
        return
    if p_score > 21:
        print("You loose! You went bust")
        return
    if d_score > 21:
        print("You win! Computer went bust")
        return
    if p_score > d_score:
        print("You win!")
        return
    print("You loose!")  


players_cards = []
score = 0
dealer_cards = []

# Deal the players and Computers Hand
for _ in range(2):
    players_cards.append(deal_card())
    dealer_cards.append(deal_card())

is_game_over = False

while not is_game_over:
    # Find out the player score
    player_score = calculate_score(players_cards)
    dealer_score = calculate_score(dealer_cards)

    # Bit of feedback
    print(f"Your cards: {players_cards}, current score: {player_score}")
    print(f"Computer's first card: {dealer_cards[0]}")

    # Do we need to end early? Player has Black Jack OR the Computer has Black Jack OR the player is bust (>21)
    if player_score == 0 or dealer_score == 0 or player_score > 21:
        is_game_over = True

    while input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
        players_cards.append(deal_card())
        player_score = calculate_score(players_cards)        
        print(f"Your cards: {players_cards}, current score: {sum(players_cards)}")
        print(f"Computer's first card: {dealer_cards[0]}")
        if player_score > 21:
            is_game_over = True
            break

    dealer_score = calculate_score(dealer_cards)
    while dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

print(f"Your final hand: {players_cards}, final score: {player_score}")
print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
compare(player_score, dealer_score)
