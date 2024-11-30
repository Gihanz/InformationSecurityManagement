#  AUTHOR:      Bruce Hansen
#  DATE         Winter 2021
#  FILE         loggingPython.py
#  FUNCTION     SHowing the difference using LOGGING and PRINT Modules
#  ==============================================
# import MODULES
import datetime
import logging

# setup variables
datNow = datetime.datetime.now()
datDate = datetime.datetime.now().date()
strLine = "-" * 25
strLineX= "=" * 40
xerr = 0

timestampZ = datNow.strftime("%Y-%m-%d  %H:%M")
timestampX = datDate.strftime("%Y%M%d")
LOG_FILENAME = "logfile_" + timestampX + ".log"

# setup logging
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO, filemode = 'w')
logging.info(timestampZ)



# set up functions
def Err_Desc(i):
    switcher={
            0:'No Errors Found',
            1:'> DATA ENTRY ERROR: Numbers were entered incorrectly',
            2:'> FUNCTION ERROR: Hypotenuse()',
            3:'>  ERR: haiudhpaiudhiuh'
    }
    return switcher.get(i,"No Error Desc Found")

def hypotenuse(a, b):
    #Compute the hypotenuse
    return (a**2 + b**2)**0.5

# CODE--------------------------------------------
print("Calculate the hypotenuse of 2 number")
a = input("enter the 1st number: ")
b = input("enter the 2nd number: ")
print("the numbers are {0} and {1}".format(a,b))
haltx = input("Enter to continue\n")
xerr= 0
strError = Err_Desc(0)
try:
    xerr = 1
    logging.info('function > Hypotenuse of {0} and {1}'.format(int(a), int(b)))
    xerr = 2
    c=round(hypotenuse(int(a), int(b)),2)

    xerr = 0
    logging.info("Hypotenuse of {0}, {1} is {2}".format(a, b, c))
    print("ANSWER: Hypotenuse of {0}, {1} is {2}".format(a, b, c))
    
except:
    logging.error("Invalid Data Entry")
    strError = Err_Desc(xerr)
'''
or can be done this way
    if xerr == 1:
        strError = "  Numbers were entered incorrectly" 
    elif xerr == 2:
        strError = "  there was an error in Hypotenuse()"  
'''
# ===================================
# LOG ENDING
logging.info("\n\n" + strLine) 
logging.info('Logging completed') 


# OUTPUT TO SCREEN
# ===================================

print("\n " + strLine)
print(datNow )
print("DONE " + strError)
    