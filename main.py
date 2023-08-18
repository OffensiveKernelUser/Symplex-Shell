shell = True
user = "guest"
device = "mainframe"

def Initialization():
    print("SymplexShell@v5.67")

def Engine():
    while shell:
        cmd = input(f"{user}@{device} ~$ ")

def Main():
    Initialization()
    Engine()

if __name__ == "__main__":
    Main()
