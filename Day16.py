# Begining of OOP

# Turtle module is a Graphics Program built into Python's download EXE
# Link to Docs: https://docs.python.org/3/library/turtle.html
# Link to Turtle Colours: https://cs111.wellesley.edu/labs/lab01/colors

# Long way
# import turtle
# timmy = turtle.Turtle()

# Shorter way
# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DarkSlateGray2")
# timmy.forward(100)

# my_screen = Screen()
# my_screen.exitonclick()

# Link to a LOT of Python Packages: https://pypi.org/
# PrettyTable docs: https://pypi.org/project/prettytable/
from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_row(["Hobart", 1357, 205556, 619.5])
table.add_row(["Sydney", 2058, 4336374, 1214.8])
table.add_row(["Melbourne", 1566, 3806092, 646.9])
table.add_row(["Perth", 5386, 1554769, 869.4])
table.align = "l"
print(table)
