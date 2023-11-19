
class Subscriber:
    def update(self, message):
        print(f'\033[92m(!) new message: {message}')

class User(Subscriber):

    def __init__(self, username, password):
        self.username =username
        self.password = password
    
    def __str__(self):
        return f'{self.username}'