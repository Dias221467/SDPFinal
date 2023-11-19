class Command:
    def __init__(self, name, description, decorator_classes = []):
        self.name = name
        self.description = description
        self.decorator_classes = decorator_classes
    
    def execute(self):
        pass

class Commands:
    def __init__(self):
        self.available_commands = {}

    def register_command(self, command):
        self.available_commands[command.name] = {
            'description' : command.description,
            'decorator' : command.decorator_classes,
            'class' : command
        }

    def import_commands(self) -> list:
        return self.available_commands