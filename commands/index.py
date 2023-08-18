"""An index of all the commands"""
from .debug.echo import echo

def interpreter(command):
    """Function to choose what command to execute"""
    if command.startswith("echo "):
        echo(command - "echo ")
    else:
        pass