shell = True
user = "guest"
device = "mainframe"

def Main():
    while shell:
        cmd = input(f"{user}@{device} ~$ ")

if __name__ == "__main__":
    Main()
