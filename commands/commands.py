class Commands:
    def __init__(self):
        self.available_commands = {}

    def register_command(self, commands):
        i = 1
        for command in commands:
            command.id = i
            self.available_commands[command.name] = {
                'id' : command.id,
                'description' : command.description,
                'decorator' : command.decorator_classes,
                'class' : command
            }
            i = i+1

    def import_commands(self) -> list:
        return self.available_commands