

class Adapter:
    def __init__(self, commands):
        self.commands = commands
        

    def adapt_input(self, user_input):
        if user_input.isnumeric():
            return self.adapt_input_by_id(user_input)
        else:
            return self.adapt_input_by_name(user_input)

    def adapt_input_by_id(self, user_input):
        for name, _ in self.commands.items():
            if int(user_input) == int(_['id']):
                return name
        return None

    def adapt_input_by_name(self, user_input):
        return user_input
