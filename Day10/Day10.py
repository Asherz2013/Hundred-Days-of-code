# Functions...

# Refresher

# Simple
def my_function():
    pass

# With input
def my_function_input(_input):
    pass

# With Output
def my_function_output(): 
    return 3 * 2

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function with multiple inputs, outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name("ASHLEY", "shaw")
print(formatted_string)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Challenge - Modify some code to make it return the number of days in a month

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year = 2021, month = 2):
    if month > 12 or month < 1:
        return "Invalid Month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    return month_days[month - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Doc Strings...
# Tooltip Intellisense
# Must be first line after function.
# Must be wrapped in 3 Quotation marks (""" """)

def function():
    """ Takes a first and last name. Formats it to return a case version of the name. """
    pass

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Challenge Calculator

from Day10_art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    """Calculation code. Runs at the start"""
    print (logo)
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print (symbol)
    should_continue = True
    while should_continue:
        operation = ""
        while operation not in operations:
            operation = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calc_function = operations[operation]
        answer = calc_function(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()