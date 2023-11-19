from commands.commands import Commands
from spotify.spotify import Spotify
from user.user import User
from adapter.adapter import Adapter
class CLI:

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(CLI, self).__new__(self)
        return self.instance
    
    def __init__(self):
        self.commands = Commands()
        self.spotify = Spotify()
        self.user = None
        self.adapter = None

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
        self.adapter = Adapter(imported_commands)
        while True:
            if self.user is None:
                self.auth()
            
            print("\nAvailable commands:")
            for name, _ in imported_commands.items():
                print(f"{_['id']}) {name} - {_['description']}")


            choice = input("Enter a command name or ID or 'exit' to quit: ")
            converted_input = self.adapter.adapt_input(choice)


            if choice == 'exit':
                print("Exiting CLI.")
                break

            if converted_input in imported_commands:
                if imported_commands[converted_input]['decorator'] is not []:
                    imported_commands[converted_input]['class'].execute(self)
                else:
                    for decorator in imported_commands[converted_input]['decorator']:
                        imported_commands[converted_input]['class'] = decorator(imported_commands[converted_input]['class'])
                    imported_commands[converted_input]['class'].execute(self)
            else:
                print("Invalid command. Please try again.")