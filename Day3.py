# Flow statement
water_level = 50
if water_level > 80:
    print("Water overflowing!")
else:
    print("Continue filling up!")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

number = int(input("Which number do you want ot check?"))

if number % 2 == 0:
    print("Number is EVEN!")
else:
    print("Number is ODD!")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Nested IF ELSE
height = 120
age = 30
if height >= 120:
    if age <= 12:
        print("$5")
    elif age <= 18:
        print("$7")
    else:
        print("$12")
else:
    print("Not tall enough")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# BMI Calculator ++
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}. You are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}. You are normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi}. You are overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}. You are obese")
else:
    print(f"Your bmi is {bmi}. You are clinically obese")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Is a Leap Yeat!!
print("")
year = int(input("Which year do you want to check?"))
# on every year that is evenly divisible by 4
#   EXCEPT every year that is evenely divisible by 100
#       UNLESS the year is also evenly divisible by 400
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("LEAP year!")
        else:
            print("Not a leap year")
    else:
        print("Leap Year")
else:
    print("Not a leap year")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Do you want a photo?
height = int(input("What is your height?"))
age = int(input("What is your age?"))
bill = 0
if height >= 120:
    if age <= 12:
        bill = 5
        print("Children tickets are £5")
    elif age <= 18:
        bill = 7
        print("Teenages tickets are £8")
    else:
        bill = 12
        print("Adult tickets are £8")
    
    wants_photo = input("Do you want a photo take? Y or N")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("Not tall enough")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Who wants PIZZA
print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want Pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

price = 0
if size == "S":
    price = 15
    if add_pepperoni == "Y":
        price += 2
else:
    if size == "M":
        price = 20
    else:
        price = 25
    if add_pepperoni == "Y":
        price += 3

if extra_cheese == "Y":
    price += 1

print(f"Your final bill is £{price}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Logic Operators AND OR NOT
bill = 0
age = int(input("What is your age?"))
if age <= 12:
    bill = 5
    print("Children tickets are £5")
elif age <= 18:
    bill = 7
    print("Teenages tickets are £8")
if age >= 45 and age <= 55:
    print("Enjoy your mid-life crisis")
else:
    bill = 12
    print("Adult tickets are £8")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Challenge
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_string = combined_string.lower()

t_count = lower_string.count("t")
r_count = lower_string.count("r")
u_count = lower_string.count("u")
e_count = lower_string.count("e")

true_total = t_count + r_count + u_count + e_count

l_count = lower_string.count("l")
o_count = lower_string.count("o")
v_count = lower_string.count("v")
e_count = lower_string.count("e")

love_total = l_count + o_count + v_count + e_count

love = (true_total * 10) + love_total

if love < 10 or love > 90:
    print(f"Your score is {love}, you go together like coke and mentos.")
elif love >= 40 and love <= 50:
    print(f"your score is {love}, you are alright together")
else:
    print(f"Your score is {love}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Choose your own adventure!
print("")
# 3 single quotes allows for Multi Line printing
# Make sure you close with 3 single quots as well
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
l_or_r = input("Left or Right?\n").lower()
if l_or_r == "left":
    swim_or_wait = input("Swim or Wait?\n").lower()
    if swim_or_wait == "wait":
        door = input("Which door? Red, Blue or Yellow?\n").lower()
        if door == "yellow":
            print("Here is your treasure!")
        else:
            print("Game over!")
    else:
        print("Game over")
else:
    print("Game over")