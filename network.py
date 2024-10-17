import os
import tempfile
from sys import argv
from is_up import function_is_up
from get_ip import function_get_ip
from lookup import function_lookup

import time

if os.name == 'nt':
    logfolder = str(tempfile.gettempdir()) + '/network_tp3'
elif os.name == 'posix':
    logfolder = '/tmp/network_tp3'

logoutput = ""
logstatus = "[INFO] "

logfile = logfolder + '/network.log'
commandlist = ["lookup","ip","ping"]
commandoutput = ""

def ping(value):
    return function_is_up(value)

def look_up(value):
    return function_lookup(value)

def ip():
    return function_get_ip()


if len(argv) < 2 :
    logstatus = "[ERROR] "
    logoutput = "Missing commands !"
    commandoutput = "Vous devez choisir une fonction"
else:
    if argv[1] in commandlist:
        if argv[1] == "ip":
            logoutput = ip()
        if argv[1] == "lookup":
            if len(argv) > 2:
                logoutput = look_up(argv[2])
            else:
                logstatus = "[ERROR] "
                logoutput = "Command lookup called with no arguments"
        if argv[1] == "ping":
            if len(argv) > 2:
                logoutput = ping(argv[2])
            else:
                logstatus = "[ERROR] "
                logoutput = "Command ping called with no arguments"
    else :
        commandoutput = f"{argv[1]} is not an available command. Déso."
        logstatus = "[ERROR] "
        logoutput = f"{argv[1]} is not an available command. Déso."

print(commandoutput)

# Gestion des logs
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
output = str(logstatus) + str(logoutput)
if not os.path.isdir(logfolder):
    os.mkdir(logfolder)
f = open(logfile, "a")
f.write(output + "\n")
f.close()