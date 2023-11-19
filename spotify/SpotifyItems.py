class SpotifyObject:
    def __init__(self, name, author):
        self.name = name
        self.author = author
    def __str__(self):
        return f'{self.name} - {self.author}'

class Music(SpotifyObject):
    def __init__(self, name, author):
        super().__init__(name=name, author=author)

    
class Album(SpotifyObject):
    def __init__(self, name, author):
        super().__init__(name=name, author=author)
    


class SpotifyArtists:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'{self.name}'

class Artist(SpotifyArtists):
    def __init__(self, name):
        super().__init__(name=name)
    
    