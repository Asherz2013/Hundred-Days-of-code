
# Loops

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Average Height (Challenge)

student_heights = input("Input a list of student heigts ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# Cant use "len" or "sum" functions...
total = 0.0
list_size = 0
for height in student_heights:
    total += float(height)
    list_size += 1
total /= list_size
total=round(total)
print(total)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Highest Score (Challenge)

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# Cant use "max" or "min" function
max_value = 0
for score in student_scores:
    if score > max_value:
        max_value = score
print(f"The highest score in the class is: {max_value}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Range function

print("")
print("Range Total")
total = 0
# Range end is NOT included. so 1 - 10 would only go to 9
for number in range(1, 101):
    total += number
print(total)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Adding Evens (Challenge)

print("")
print("Adding Evens")
total = 0
for number in range(0 , 101, 2):
    total += number
print(total)

total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Fizz Buzz (Challenge)

print("")
print("Fizz Buzz")
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Password Generator (Challenge)
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for letter in range(0, nr_letters):
    password += random.choice(letters)

for symbol in range(0, nr_symbols):
    password += random.choice(symbols)

for number in range(0, nr_numbers):
    password += random.choice(numbers)
print("Easy: " + password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for letter in range(0, nr_letters):
    password_list += random.choice(letters)

for symbol in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for number in range(0, nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char

print("Hard: " + password)