import socket
from socket import gethostbyname
import os
from sys import argv
import re


def function_lookup(value):
    if value == "" :
        print("Il manque un argument'")
    elif not re.search(r'\.', value):
        print(f"Command lookup called with bad arguments : {value}")
        return f"Command lookup called with bad arguments : {value}:"
    else:
        try:
            print(socket.gethostbyname(value))
            return f"Command lookup called successfully with argument {value}"
        except socket.gaierror:
            print("Nom d'hôte invalide")
            return "Command lookup called with bad arguments :"

if __name__ == "__main__":
    if len(argv) > 1:
        function_lookup(argv[1])
    else:
        print("Il manque un argument")