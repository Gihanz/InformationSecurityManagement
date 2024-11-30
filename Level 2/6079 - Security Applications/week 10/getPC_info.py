
#  AUTHOR:       Bruce Hansen
#  DATE          April 2021
#  COURSE        INFO-6079   Winter 2021
#  FUNCTION      LAB 10
#  ==============================================
# import MODULES
import datetime
import logging
import platform

# setup variables
datNow = datetime.datetime.now()
datDate = datetime.datetime.now().date()
strLine = "-" * 25
strLineX= "=" * 40
xerr = 0

timestampZ = datNow.strftime("%Y-%m-%d  %H:%M")
timestampX = datDate.strftime("%Y%M%d")
LOG_FILENAME = "LAB_logfile_" + timestampX + ".log"
INFO_FILE = "INFO_PC_" + timestampX + ".txt"
# LOGGING
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO, filemode = 'w')
logging.info("PC LOG Info\n" + strLineX)
logging.info("\n") 
logging.info(timestampZ)


# CODE  ===========================================
try:
    file1 = open(INFO_FILE, "w")     
    strError = "No Errors Found"
    file1.writelines( timestampZ )
    file1.writelines("\nMachine Data\n")
    file1.writelines(strLine )
    file1.writelines("\nMachine\t\t" + platform.machine())
    file1.writelines("\nVersion\t\t" + platform.version())
    file1.writelines("\nPlatform\t" + platform.platform())
    file1.writelines("\nSystem\t\t" + platform.system())
    file1.writelines("\nProcessor\t" + platform.processor())

except:
    logging.error("PC Info Data Error")
    strError = "PC info Data Errors"
    
# ===================================
# LOG ENDING
logging.info("\n" + strLine) 
logging.info("Logging completed " + strError) 
    
    
# OUTPUT TO FILE
# ===================================
file1.writelines( "\n" + strLine )
file1.writelines( "\n" + timestampZ )
file1.writelines( "\nDONE " + strError)

# OUTPUT TO SCREEN to show is done
# ===================================
print("Run Completed",timestampZ )