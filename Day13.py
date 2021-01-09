############DEBUGGING#####################

# Describe Problem
# # Problem - Print is NOT being printed
# # Solution - "range" end is excluded, meaning that it is NOT counted in the loop. So we either up the end by 1 OR we reduce the IF check by 1
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
# # Problem - At a random point, this will produce the following stack trace:
# """
# Traceback (most recent call last):
#   File "d:/Programming/Python/Hundred Days of code/Day13.py", line 18, in <module>
#     print(dice_imgs[dice_num])
# IndexError: list index out of range
# """
# # Solution - Array is ZERO indexed, so the Random could return 6 but this would be out of bounds of the array 0 - 5. Reduce the randint to 0 - 5 OR -1 from dice_num before using it
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# Play Computer
# # Problem - Upon entering 1994 - Nothing gets printed
# # Solution - 1994 is not checked in Either IF statement. Either <= 1994 in the first IF OR >= 1994 in the ELIF
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# Fix the Errors
# # Problem - PRINT was showing squiggly lines under it. 
# # - When ran we get the following stack trace:
# """
# Traceback (most recent call last):
#   File "d:/Programming/Python/Hundred Days of code/Day13.py", line 39, in <module>
#     if age > 18:
# TypeError: '>' not supported between instances of 'str' and 'int'
# """
# # - {age} was not showing up as the right age.
# # Solution - IF PRINT was intended to be part of the IF above it, then we need to indent it. Otherwise we should PASS / Do something else there.
# # - Need to convert the input to an INT to be compared to an INT
# # - Need to convert the String to an F string
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

#Print is Your Friend
# # Problem - Upon running the output is ZERO
# # Solution - After using PRINT to see what is coming out of these I can see there is a DOUBLE = sign on the INPUT of Words Per Page.
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"Pages: {pages}")
# print(f"Words per Page: {word_per_page}")
# print(total_words)

#Use a Debugger
# # Problem - Once run the output is just [26]
# # Soultion - After using the debugger, I can see that the List is generated correctly. However when it is stepping through the provided list the new value is being created but NOT pushed into the new Array. Indentation is the issue here, just indent the APPEND into the new list so it is part of the FOR LOOP.
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TIPS
"""
* Take a Break
* Ask a Friend (Another programmer)
* Run your code often. Means you are testing small changes
* Look online - Maybe Stack Overflow
"""