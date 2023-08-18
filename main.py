"""Module providing colors for the shell"""
from utilities.colors import COLORS

SHELL = True
USER = "guest"
DEVICE = "mainframe"

def initialization():
    """Function to initialize the shell"""
    print(f"{COLORS['WHITE']}SymplexShell@v5.67")

def engine():
    """Main shell engine"""
    while SHELL:
        CMD = input(f"{COLORS['WHITE']}{USER}@{DEVICE} ~$ ")

def main():
    """Main function"""
    initialization()
    engine()

if __name__ == "__main__":
    main()
