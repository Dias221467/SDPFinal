from conf import cli
from commands.custom_commands import *

def main():
    cli.commands.register_command([HelloWordCommand, AddSpotifyItem, DisplaySpotifyItems, DisplaySpotifyMusic, DisplayArtists, AddArtists, Subscribe])
    cli.run()

if __name__ == '__main__':
    main()
