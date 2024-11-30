# =========================================================
#	NAME:		GIHAN SHAMIKE LIYANAGE (1142109)
#	DATE:		SUMMER WEEK 11 2023
#	Function	Lab 9 Code Solution
#			Python 3.11.3
#			WING Personal 9
# =========================================================

import os
import platform

# Print Current Working Directory (CWD)
cwd = os.getcwd()
print("Current Working Directory (CWD):", cwd)

# Print files and directories in the current Directory
print("\nFiles and directories in current Directory:")
for item in os.listdir(cwd):
    print(item)

# Use the walk() function to print files in a given directory
filePath = "C:\\Users\\Gihan\\Downloads"
print("\nFiles in the path given:", filePath)
for root, _, files in os.walk(filePath):
    for fileName in files:
        print(fileName)

# Print Host's OS information
host_os_info = platform.platform()
print("\nHost's OS information:", host_os_info)
        
# Get and print the host's processor information
host_processor_info = platform.processor()
print("Host's processor info:", host_processor_info)
        
# Get and print the Python version on the host machine
py_version = platform.python_version()
print("Host's Python version:", py_version)
        
# Save output to a text file
output_file = "GS_lab_week11_results.txt"
with open(output_file, "w") as h:
    h.write("Host's OS information: " + host_os_info + "\n")
    h.write("Host's processor info: " + host_processor_info + "\n")
    h.write("Host's Python version: " + py_version + "\n")

print("\nResults saved to", output_file)