# Random -> Mersenne Twister
import random
import my_module # This is my OWN file

# How to seperate code into different Python files.
print(my_module.pi)

# Numbers are INCLUSIVE
random_int = random.randint(1,10)
print(random_int)

# 0.0 - 0.9...
random_float = random.random()
print(random_float)

# 0.0 - 4.9...
random_float = random_float * 5
print(random_float)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

side = random.randint(0,1)
if side == 1:
    print("Heads")
else:
    print("Tails")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Lists

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]
# Standard index of the List
print(states_of_america[0])
# -1 is the last item in the list. As you go more negative you read from the back
print(states_of_america[-1])
# Add to the end
states_of_america.append("New Land")
# Add LOTS
states_of_america.extend(["Another Land", "One More Land"])
# prints the list
print(states_of_america)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Challenge
print("")
print("[Challenge] Who buys the meal generator")
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's name, sperated by a comma. ")
names = namesAsCSV.split(", ")

index = random.randint(0, len(names)-1)
person = names[index]
print(f"{person} is going to buy the meal today")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Nested Lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegatables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegatables]
print(dirty_dozen)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Challenge
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])-1
vertical = int(position[1])-1

map[vertical][horizontal] = "X"

print(f"{row1}\n{row2}\n{row3}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Rock Paper Scissors

print("")
print("Rock Paper Scissors!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

selection = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if player_choice < 0 or player_choice >= 3:
    print("Please choose a different number. You Loose")
else:
    print(selection[player_choice])
    ai_choice = random.randint(0,2)
    print("Computer chose:")
    print(selection[ai_choice])

    if player_choice == ai_choice:
        print("Its a Draw!")
    else:
        if player_choice == 0:
            if ai_choice == 2:
                print("You win")
            else:
                print("You lose")
        elif player_choice == 1:
            if ai_choice == 0:
                print("You win")
            else:
                print("You loose")
        else:
            if ai_choice == 1:
                print("You win")
            else:
                print("You lose")
