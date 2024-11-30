#  DATE             Fall 2020
#  FUNCTION     Admin code

import subprocess
import os
import getpass
import socket
import datetime
datNow = datetime.datetime.now()
datDate = datetime.datetime.now().date()

strSeparator = "-" * 50
#dir_path = os.path.dirname(os.path.realpath(__file__))
#print("Current Folder\t", dir_path)

##Write a Python program to get the current username.
#print("User ID\t\t",getpass.getuser())

#homedir = os.path.expanduser("~")
#print("Home Directory\t", homedir)

#hostname = socket.gethostname()
#print("Host Name\t", hostname)

# DIR
print(strSeparator)
print('DIR >')
subprocess.run(['dir'], shell=True)

# ARP
print(strSeparator)
print('ARP >')
subprocess.run(["arp", "-a"])

# write completed code - no errors
print(strSeparator)
print("Python Completed",datNow)




