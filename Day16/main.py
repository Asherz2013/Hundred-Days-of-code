from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Write code below this line

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    # 1. Print report
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if drink is not None:
            # 2. Check resources sufficient?
            if coffee_maker.is_resource_sufficient(drink):
                # 3. Process coins.
                print(f"A {drink.name} costs ${drink.cost}")
                # 4. Check Transaction successful?
                if money_machine.make_payment(drink.cost):
                    # 5. Make Coffee
                    coffee_maker.make_coffee(drink)
        else:
            print("This drink is not available.")
