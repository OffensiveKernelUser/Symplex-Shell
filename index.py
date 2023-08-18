"""An index of all the commands"""
from utilities.colors import COLORS
from commands.debug.echo import echo

def interpreter(command):
    """Function to choose what command to execute"""
    if command.startswith("echo "):
        echo(command)
    elif command == "":
        pass
    else:
        print(f"{COLORS['RED']}Error: Unknown command\nTry installing a package containing the command {command.split(' ')[0]}")
