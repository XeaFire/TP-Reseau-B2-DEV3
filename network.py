import os
import tempfile
from sys import argv
from is_up import function_is_up
from get_ip import get_ip
from lookup import function_lookup

import time

logoutput = ""
logstatus = "[INFO] "
logfolder = str(tempfile.gettempdir()) + '/network_tp3'
logfile = logfolder + '/network.log'
commandlist = ["lookup","ip","ping"]
commandoutput = ""

def ping(value):
    function_is_up(value)

def look_up(value):
    return function_lookup(value)

def ip():
    get_ip.get_ip()


if len(argv) < 2 :
    commandoutput = "Vous devez choisir une fonction"
else:
    if argv[1] in commandlist:
        if argv[1] == "ip":
            ip()
        if argv[1] == "lookup":
            if len(argv) > 2:
                logoutput = look_up(argv[2])
        if argv[1] == "ping":
            if len(argv) > 2:
                ping(argv[2])
    else :
        commandoutput = f"{argv[1]} is not an available command. Déso."
        logstatus = "[ERROR] "
        logoutput = f"{argv[1]} is not an available command. Déso."

print(logoutput)

# Gestion des logs
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
output = str(logstatus) + str(logoutput)
print(output)
if not os.path.isdir(logfolder):
    os.mkdir(logfolder)
f = open(logfile, "a")
f.write(output + "\n")
f.close()