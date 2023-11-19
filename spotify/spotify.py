from .spotifyFabric import SpotifyFabric

from .SpotifyItems import Music, Album

class Spotify:
    
    def __init__(self):
        self.fabric = SpotifyFabric()
        self.items = []
        self.artists = []
        self.subscribers = []

    def addItem(self, itemType, name, author):
        self.items.append(self.fabric.create_item(itemType, name, author))
        self.notifySubscribers(f'Added New item - {self.items[-1]}\033[0m')

    def displayItems(self):
        for item in self.items:
            print(item, sep='\n')

    def displayMusic(self):
        for item in self.items:
            if item.__class__ == Music:
                print(item)
    
    def registerArtists(self, name):
        self.artists.append(self.fabric.create_item('artist', name, ''))

    def displayArtists(self):
        for item in self.artists:
            print(item, sep='\n')
    
    def addSubscriber(self, user):
        if user not in self.subscribers:
            self.subscribers.append(user)
            print('\033[92mSuccessfully subscribed!\033[0m')
        else:
            print(f'\033[91m{user} is already subscribed!\033[0m')

    def notifySubscribers(self, message):
        for item in self.subscribers:
            item.update(message)
    