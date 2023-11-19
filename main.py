from cli.cli import CLI
from commands.custom_commands import HelloWordCommand

def main():
    cli = CLI()
    cli.commands.register_command(HelloWordCommand)
    cli.run()

if __name__ == '__main__':
    main()
