import os
from os import system
from sys import argv

def ping_arg():
    if len(argv) < 2 :
        print("Il manque un argument'")
    else:
        os.system(f"ping {argv[1]}")
        return 

if __name__ == "__main__":
    ping_arg()