class User:
    pass  # we can use if we don't have anything to update anything as of now

    def __int__(self):
        print("new user has been created")


user_1 = User()
user_1.id = "001"
user_1.username = "savithri"
print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "gayathri"
