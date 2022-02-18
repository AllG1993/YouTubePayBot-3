

class User:
    def __init__(self, tg_user_id):
        self.tg_user_id = tg_user_id


if __name__ == '__main__':
    user_1 = User(123456789)
    print(user_1.tg_user_id)
