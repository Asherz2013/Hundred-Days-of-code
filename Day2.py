print("Hello"[0])
# ^ Prints 'H' - SubString

123_456_789
# ^ Will read back as 123456789, but is easier to read

print(type(123))
# ^ Prints out what TYPE the input is

# Convertions
str(123) # Int to String
int("123") # String to Int
float("123.3") # String to Float
int(123.4) # Float to INT

two_digit_number = input("Type a two digit number: ")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
print (first_digit + second_digit)

# Mathamtical Operators
3 + 5
7 - 4
3 * 2
6 / 3 # <- Always returns a FLOAT
2 ** 3 # EXPONENT (Power) 2 * 3 = 8

# Flow
# PEMDAS
# ()
# **
# * /
# + -

3 * 3 + 3 / 3 - 3 # = 7
3 * (3 + 3) / 3 - 3 # = 3

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# BMI Calculator
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
bmi = int(int(weight) / float(height) ** 2)
print(str(bmi))

# Rounding
8 / 3 # = 2.666666666665
int(8 / 3) # = 2
round(8 / 3) # 3
round(8 / 3, 2) # 2.67
# // -> FLOOR DIVISION
8 // 3 # = 2 (always a INT)

# F-String
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Your Life in weeks
age = input("What is your current age? ")
age_int = int(age)
years_remaining = 90 - age_int
days = years_remaining * 365
weeks = years_remaining * 52
months = years_remaining * 12
print(f"You have {days} days, {weeks} weeks and {months} months left.")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Tip Calculator

print("")
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
per_person = (percentage / 100 * bill + bill) / people
per_person_round = round(per_person,2)
print(f"Each person should pay: ${per_person_round}")