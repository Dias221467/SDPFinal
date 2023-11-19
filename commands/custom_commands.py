from conf import cli
from .decorators import WarnCommandDecorator
class Command:
    def execute(self):
        pass

class HelloWordCommand(Command):
    name = 'Hello World'
    description = 'Prints Hello World'
    decorator_classes = []
    
    def execute(self):
        print('Hello Worldwefljnwef')
    
class AddSpotifyItem(Command):
    name = 'AddItem'
    description = 'Add Music Or Album to spotify'
    decorator_classes = []
    
    def execute(self):
        item = input('Item type (music, album): ')
        name = input('Name: ')
        author = input('Author: ')
        cli.spotify.addItem(item, name, author)

class DisplaySpotifyItems(Command):
    name = 'DisplayItems'
    description = 'Display Items in spotify'
    decorator_classes = []

    def execute(self):
        cli.spotify.displayItems()

class DisplaySpotifyMusic(Command):
    name = 'DisplayMusic'
    description = 'Display music in spotify'
    decorator_classes = []

    def execute(self):
        cli.spotify.displayMusic()

class DisplayArtists(Command):
    name = 'DisplayArtists'
    description = 'Display All Artists'
    decorator_classes = []

    def execute(self):
        cli.spotify.displayArtists()

class AddArtists(Command):
    name = 'AddArtists'
    description = 'Register Artist'
    decorator_classes = []

    def execute(self):
        name = input('Enter Artist name: ')
        cli.spotify.registerArtists(name)

class Subscribe(Command):
    name = 'Subscribe'
    description = 'Subscribe to spotify news'
    decorator_classes = [WarnCommandDecorator]

    def execute(self):
        cli.spotify.addSubscriber(cli.user)