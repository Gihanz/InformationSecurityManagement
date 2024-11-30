# =========================================================
#	NAME:		GIHAN SHAMIKE LIYANAGE (1142109)
#	DATE:		SUMMER WEEK 12 2023
#	Function	Lab 10 Code Solution
#			Python 3.11.3
#			WING Personal 9
# =========================================================

# Import modules 
import platform
import logging
from datetime import datetime

# Write to GS_Lab10_output.txt
initials = "GS"
txt_filename = f"{initials}_Lab10_output.txt"
log_filename = f"{initials}_Lab10_output.log"
logging.basicConfig(filename=log_filename, level=logging.INFO, filemode = 'a')

# Create variables using strftime()
current_date_with_time = datetime.now().strftime('%Y-%m-%d %H:%M')
current_date_no_time = datetime.now().strftime('%Y-%m-%d')

try:
    strError = "No Errors Found"
    
    txt_file = open(txt_filename, 'w')
    txt_file.writelines(current_date_with_time)
    txt_file.writelines("\nMachine Data:\n")
    txt_file.writelines("-------------------------------------------------\n")
    txt_file.writelines(f"Machine   \t{platform.machine()}\n")
    txt_file.writelines(f"Version   \t{platform.version()}\n")
    txt_file.writelines(f"Platform  \t{platform.platform()}\n")
    txt_file.writelines(f"System    \t{platform.system()}\n")
    txt_file.writelines(f"Processor \t{platform.processor()}\n")
    txt_file.writelines("-------------------------------------------------\n")
    txt_file.writelines(current_date_with_time)
    txt_file.writelines("\nDone " + strError)    
    
    logging.info("PC LOG Info\n======================")
    logging.info("\n")
    logging.info(current_date_with_time)
    logging.info("\n--------------------")
    logging.info("Logging Completed " + strError)
    
except Exception as strError:
    logging.error("PC Info Data Error")
    logging.info("Logging completed " + str(strError))
    

print("Run Completed",current_date_with_time)
