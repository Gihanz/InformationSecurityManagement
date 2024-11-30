# =========================================================
#	NAME:		GIHAN SHAMIKE LIYANAGE
#	Student ID:	1142109
#	DATE:		08/08/2023
#
#			FINAL PRACTICAL TEST
#			Python 3.11.3
#			WING Personal 9
# =========================================================

# Import modules 
import logging
import datetime
import os
import platform

# ========================= PART 2 =========================

# Configure logging
logging.basicConfig(filename='log_file.log', level=logging.INFO, filemode = 'a')

# Insert name and Student ID
name = "Gihan Shamike Liyanage"
student_id = "1142109"
logging.info("Name: %s, Student ID: %s", name, student_id)

# Insert programmed Current Date
current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
logging.info("Programmed Current Date: %s", current_date)

# Read data from a text file and insert into the log file
data_file_name = "(gliyanage)_final_test.txt"
try:
    with open(data_file_name, "r") as data_file:
        data = data_file.read()
        logging.info("Data from %s:\n%s", data_file_name, data)
except FileNotFoundError:
    logging.error("Failed to read data from %s: File not found.", data_file_name)

print("Part 2 log data written to log_file.log\n")



# ========================= PART 3 =========================

class NumberAdder:
    __private_class_var = 0
    
    def __init__(self):
        self.__total = 0

    def _ADD_NUMBER(self):
        while True:
            user_input = input("Enter a number (press ENTER to stop): ")
            if user_input == "":
                break
            try:
                number = float(user_input)
                self.__total += number
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        print("Total:", self.__total)
        

number_adder = NumberAdder()
number_adder._ADD_NUMBER()

# Print Current Working Directory (CWD)
cwd = os.getcwd()
print("\nCurrent Working Directory (CWD):", cwd)

# Print files and directories in the current Directory
print("\nFiles and directories in current Directory:")
for item in os.listdir(cwd):
    print(item)

# Insert Laptop OS information to log_file.log 
logging.info("------------ Laptop OS information --------------")
logging.info(f"System    \t{platform.system()}")
logging.info(f"Version   \t{platform.version()}")
logging.info(f"Platform  \t{platform.platform()}")
logging.info("-------------------------------------------------")

# Insert current version of Python to log_file.log 
logging.info(f"Python version    \t{platform.python_version()}")

# Create a new Folder and insert name to log_file.log 
folder_name = "g_liyanage_folder"
try:
    os.mkdir(folder_name)
    logging.info("New folder - '{}' created.".format(folder_name))
except Exception as e:
    logging.error("Failed to create folder '{}': {}".format(folder_name, str(e)))
    
print("\nRun Completed",current_date)