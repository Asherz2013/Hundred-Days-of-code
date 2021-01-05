# Modifying Global Scope Variables
enemies = 1

# def increase_enemies():
#     enemies += 1 # Here is an error
#     print(f"enemies inside function: {enemies}")

# To resolve the above
def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# General practice is to avoid modifying Global Scope variables, so the above is BAD!
# A way around the above is to return the Global plus any modification that needs to take place.