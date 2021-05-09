# Dictionaries and Nesting

# Simple definition {key: value}
# Multiple definition:
# {
#   key:value,
#   key2:value
# }

#programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",  
}
print(programming_dictionary)

# Syntax - Getting key is CASE Sensitive - ALso make sure they are the same TYPE
print(programming_dictionary["Bug"])

# Add a new entry
programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary)

#Create an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Looping
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Challenge - Grading Program

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

# Nesting Lists and Dictionaries
# {
#   key: [List],
#   key2: {Dict},
# }

captials = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a Dictionary in a Dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
        },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
        },
}

#Nesting a Dictionary in a List
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Coding Challenge - Dictionary in List

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)

    # travel_log.append({
    #     "country": country,
    #     "visits": visits,
    #     "cities": cities
    # })

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Blind auction

import os
clear = lambda: os.system('cls')
clear()
#HINT: You can call clear() to clear the output in the console.
from Day9_art import logo

blind_action = {}

print(logo)

def ask_for_bid():
    name = input("What is your name? ")
    price = int(input("What is your bid? £"))
    blind_action[name] = price

    more_people = input("Are there any other bidders (yes / no)? ").lower()
    if more_people == "yes":
        clear()
        ask_for_bid()
    
ask_for_bid()

winning_name = ""
winning_price = 0

for bid in blind_action:
    price = blind_action[bid]
    if price > winning_price:
        winning_name = bid
        winning_price = price
print(f"The winner was {winning_name} with a price of £{winning_price}")