"""Main program"""
from commands.index import interpreter
from utilities.colors import COLORS

SHELL = True
VERSION = "5.67"
USER = "guest"
DEVICE = "mainframe"

def initialization():
    """Function to initialize the shell"""
    print(f"{COLORS['WHITE']}SymplexShell@v{VERSION}")

def engine():
    """Main shell engine"""
    while SHELL:
        cmd = input(f"{COLORS['WHITE']}{USER}@{DEVICE} ~$ ")
        interpreter(cmd)

def main():
    """Main function"""
    initialization()
    engine()

if __name__ == "__main__":
    main()
