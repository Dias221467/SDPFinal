from commands.commands import Commands

class CLI:

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(CLI, self).__new__(self)
        return self.instance
    
    def __init__(self):
        self.commands = Commands()


    def run(self):
        imported_commands = self.commands.import_commands()
        print(imported_commands)
        while True:
            print("\nAvailable commands:")
            for name, _ in imported_commands.items():
                print(f"{name} - {_['description']}")


            choice = input("Enter a command name or ID or 'exit' to quit or 'logout' to logout: ")

            if choice == 'exit':
                print("Exiting CLI.")
                break

            if choice in imported_commands:
                imported_commands[choice]['class'].execute([])
            else:
                print("Invalid command. Please try again.")