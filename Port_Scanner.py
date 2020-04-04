import sys
import socket
from datetime import datetime

#Define our Target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4

else:
    print("Invalid amount of Arguments.")
    print("Syntax: python3 Port_scanner <ip>")

#Add a Banner
print("-" * 50)
print("Scanning Target:" +target)
print("Time Started:" +str(datetime.now()))
print("-" * 50)

try:
    for port in range(21,81):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #returns an error indicator
        print("Checking Port {}".format(port))
        if result == 0:
            print("Port {} is open. ".format(port))
        s.close()
except KeyboardInterrupt:       #using Ctrl+C to stop exec.
    print("\nExiting Program....")
    sys.exit()

except socket.gaierror:        #Wrong hostname or ip:192.168.257.1
    print("Hostname couldn't be resolved.")
    sys.exit()

except socket.error:            #Network not found
    print("couldn't connect to the server.")
    sys.exit()