class User:
    def __init__(self, id, username):
        print("New user being created....")
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user_1 = User("007", "James Bond")
print(user_1.id)
#user_1.username = "James Bond" same as passing the value of attribute while creating an object
print(user_1.username)
#print(user_1.followers)
user_2 = User("001", "Aryan Srivastava")
print(user_2.id)
print(user_2.username)
user_2.follow(user_1)
print("user 2 is following user 1")
print(f"Followers of user 1 = {user_1.followers}")
print(f"Following of user 2 = {user_2.following}")