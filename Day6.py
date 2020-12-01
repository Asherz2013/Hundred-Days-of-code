# Functions

def my_function():
    print("Hello")
    print("Bye")

my_function()

#~~~~~~~~~~~~~~~~~~~~~~~~
# Challenge
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

#~~~~~~~~~~~~~~~~~~~~~~~~
# Indentation is IMPORTANT!
# It makes sure blocks of code work together

def my_other_function():
    print("Part of my Function")
print("NOT part of my function")

#~~~~~~~~~~~~~~~~~~~~~~~~
# While loop

number_of_hurdles = 6
while number_of_hurdles > 0:
    # do something
    number_of_hurdles -= 1

#~~~~~~~~~~~~~~~~~~~~~~~~~
# Challenge
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

#~~~~~~~~~~~~~~~~~~~~~~~~~
# Challenge
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

#~~~~~~~~~~~~~~~~~~~~~~~~~
# Challenge
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# Code:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     while not right_is_clear():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

#~~~~~~~~~~~~~~~~~~~~~~~~~
# Final Challenge
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Code:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# This while loop is for HARD debuging, where the bot can get into an infinate loop.
# It makes sure the bot has a wall on its right before we try and reach the goal
# while front_is_clear():
#     move()
# turn_left()
    
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()