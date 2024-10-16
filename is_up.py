import os
from os import system
from sys import argv

def function_is_up(value):
    if len(argv) < 2 and value == "" :
        print("Il manque un argument'")
    else:
        if value == "":
            value = argv[1]
        response = os.system(f"ping {value} > ./lapoubelle")
        if response == 0:
            print("UP !")
        else:
            print("DOWN !")
    

if __name__ == "__main__":
    function_is_up(argv[1])