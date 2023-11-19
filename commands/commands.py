class Commands:
    def __init__(self):
        self.available_commands = {}

    def register_command(self, commands):
        for command in commands:
            self.available_commands[command.name] = {
                'description' : command.description,
                'decorator' : command.decorator_classes,
                'class' : command
            }

    def import_commands(self) -> list:
        return self.available_commands