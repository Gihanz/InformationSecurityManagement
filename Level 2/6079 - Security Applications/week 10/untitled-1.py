#  FUNCTION     Week 12 LAB Support
#  DATE         APRIL 2020 - Week 12

#--------------------------------------------------
# import modules
import subprocess
import socket
import ipaddress

from datetime import date
datDate = date.today()

# start
print(datDate, "Lab 10 Week 12 coding lab")
print("-" * 40)


# sample code only
with open( strFilename , 'w+') as strF:
    print("out to file", strFilename)
    pFile = subprocess.run(["dir", "-l"])
    print(pFile.stdout)