class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0


user_1 = User("001", "savithri")
user_2 = User("002", "gayathri")
print(user_1)
print(user_2)
