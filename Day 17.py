

class User:

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User(user_id='001', user_name='RZRZ')
user2 = User(user_id='002', user_name='ZZZZ')

user1.follow(user2)
print(user1.name, user1.id, user1.followers, user1.following)
print(user2.name, user2.id, user2.followers, user2.following)

