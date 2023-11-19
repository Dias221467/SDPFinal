from .SpotifyItems import SpotifyObject, Music, Album, Artist

class SpotifyFabric():
    def create_item(self, itemType, name, author):
        if itemType == 'music':
            item = Music(name, author)
            return item
        elif itemType == 'album':
            item = Album(name, author)
            return item
        elif itemType == 'artist':
            item = Artist(name)
            return item
        else :
            return None