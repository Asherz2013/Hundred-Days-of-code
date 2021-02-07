# Virtual Coffee Machine Project

# Make 3 types of drinks
# 1. Espresso
# 2. Latte
# 3. Cappuccino

# Ingredients for each
# 1.                # 2.                # 3.
# 50ml Water        # 200ml Water       # 250ml Water
# 18g Cofee         # 24g Coffee        # 24g Coffee
#                   # 150ml Milk        # 100ml Milk

# Price for each
# 1.                # 2.                # 3.
# $1.50             # $2.50             # $3.00

# Coin operated... (Using US coins...)
# 4 Types of coin
# Penny     = $0.01
# Nickel    = $0.05
# Cent      = $0.10
# Quarter   = $0.25

# Operations required
# 1. Get a Report on Resources
# 2. Check Resources are sufficient
# 3. Process coins
# 4. Check transaction successful
# 5. Make Coffee
# 6. Reduce Resources

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def checksufficientresources(ingredients):
    """Returns True when order can be made, False if ingredients are
    insufficient"""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def processmoney(coffee):
    """Returns True or False, after calcualting total coin input"""
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many cents?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_recieved, drink_cost):
    """Return True when payment is accepted, False if money is insufficient"""
    change = 0
    if money_recieved < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_recieved > drink_cost:
        change = round(money_recieved - drink_cost, 2)
    # We know there is enough change. So lets add it to the machine
    # Need to add the Global keyword to let this function know that "profit"
    # is a Global variable, not local
    global profit
    profit += drink_cost
    # Check for Change...
    if change > 0:
        print(f"Here is ${change} dollars in change.")
    return True


def makecoffee(drink_name, ingredients):
    """Actually make the coffee the user has requested"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Please enjoy your {drink_name}")


is_on = True

while is_on:
    # Store users decision
    decision = ""
    # If it is not a VALID option, run it again
    while decision not in MENU and decision not in ["report", "off"]:
        decision = input("What would you like? (espresso/latte/cappuccino): ")
    # If it is OFF. Just return
    if decision == "off":
        print("Powering down...")
        is_on = False
    # If its asking for the REPORT. Print it
    elif decision == "report":
        print("Resource Report")
        for resource in resources:
            if resource not in "coffee":
                print(f"{resource}: {resources[resource]}ml")
            else:
                print(f"{resource}: {resources[resource]}g")
        print(f"Money: ${profit}")
    # At this point we know we are trying to make a coffee
    else:
        # Check resources
        if checksufficientresources(MENU[decision]["ingredients"]):
            payment = processmoney(decision)
            if is_transaction_successful(payment, MENU[decision]["cost"]):
                makecoffee(decision, MENU[decision]["ingredients"])
