# Classes

# PascalCase for Class names
# snake_case for all other variables

# Can use "pass" like in functions to generate empty code (same for funcitons)

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # Below is just a default value
        self.followers = 0


# This is a bad way to do this. Should make them Class Attributes
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Ashley"

# Below is the proper way to do it :D
user_1 = User("001", "Ashley")

print(user_1.username)
