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
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# This is a bad way to do this. Should make them Class Attributes
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Ashley"

# Below is the proper way to do it :D
user_1 = User("001", "Ashley")
user_2 = User("002", "Jack")

user_1.follow(user_2)

print(f"{user_1.username}: Following Count - {user_1.following} Followers Count - {user_1.followers}")
print(f"{user_2.username}: Following Count - {user_2.following} Followers Count - {user_2.followers}")
