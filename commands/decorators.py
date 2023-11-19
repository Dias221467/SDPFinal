from conf import cli

class CommandDecorator():
    def __init__(self, command):
        self._command = command

    def execute(self):
        self._command.execute()


class WarnCommandDecorator(CommandDecorator):
    def execute(self):
        self._command.execute(self)
        print(f"Warning: {cli.user} - executed {self._command.name}")
