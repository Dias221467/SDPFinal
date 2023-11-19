from .commands import Command

class HelloWordCommand(Command):
    name='Hello World'
    description='Prints Hello World'
    decorator_classes=[]
    def __init__(self):
        super().__init__(name=self.name, description=self.description, decorator_classes=self.decorator_classes)
    
    def execute(self):
        print('Hello Worldwefljnwef')
    