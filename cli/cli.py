from commands.commands import Commands
from spotify.spotify import Spotify
from user.user import User
class CLI:

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(CLI, self).__new__(self)
        return self.instance
    
    def __init__(self):
        self.commands = Commands()
        self.spotify = Spotify()
        self.user = None

    def auth(self):
        from conf import users
        username = input('Enter username: ')
        password = input('Enter password: ')
        try:
            if users[username] == password:
                curr_user = User(username, password)
                self.user = curr_user
                print(f'Welcome, {username}')
                return
        except KeyError:
            print('Invalid credentials! Try again!')
            return self.auth() 


    def run(self):
        imported_commands = self.commands.import_commands()
        while True:
            if self.user is None:
                self.auth()
            
            print("\nAvailable commands:")
            for name, _ in imported_commands.items():
                print(f"{name} - {_['description']}")


            choice = input("Enter a command name or ID or 'exit' to quit: ")

            if choice == 'exit':
                print("Exiting CLI.")
                break

            if choice in imported_commands:
                imported_commands[choice]['class'].execute([])
            else:
                print("Invalid command. Please try again.")