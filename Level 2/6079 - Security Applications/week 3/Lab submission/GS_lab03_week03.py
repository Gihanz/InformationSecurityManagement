# =========================================================
#	NAME:		GIHAN SHAMIKE LIYANAGE
#	DATE:		SUMMER WEEK 3 2023
#	Function	Lab 3 Code Solution
#			Python 3.11.3
#			WING Personal 9
# =========================================================

import datetime
import subprocess

# Set current date and time
current_datetime = datetime.datetime.now()

# Get birthday as input
year = int(input("Enter birth year: "))
month = int(input("Enter birth month: "))
day = int(input("Enter birth day: "))

# Set datetime object for birthday
birthday = datetime.datetime(year, month, day)

# Calculate and print age
age = (current_datetime - birthday).days // 365
print("Age: {:.0f} years".format(age))

# Print start date
formatted_date = current_datetime.strftime("Date: %B %d, %Y")
print(formatted_date)

# Print start time
print("Start time: {0}:{1}:{2}".format(current_datetime.hour, current_datetime.minute, current_datetime.second))



# Ping a website
website = input("Enter website to ping: ")
ping_count = int(input("Enter number of times to ping: "))
ping_command = f"ping -n {ping_count} {website}"
subprocess.run(ping_command, shell=True)

# Run NETSTAT
netstat_command = "netstat"
subprocess.run(netstat_command, shell=True)

# Set end time of the script
end_datetime = datetime.datetime.now()

# Calculate time difference
time_difference = end_datetime - current_datetime
print(f"Script execution time: {time_difference}")

