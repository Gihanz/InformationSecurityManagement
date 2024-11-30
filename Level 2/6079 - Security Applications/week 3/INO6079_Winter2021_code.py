#  FUNCTION     Week 3 code
#  AUTHOR       Bruce Hansen
#  DATE         January 2021
#  DESCRIPTION  Lesson 3 for Info 6079
#  REVISION     1.002
#      Dates 
#      Datetime module
#      String formatting
#      working with files 
#  ---------------------------------------------
# using the module: datetime
import datetime
#ISO standard format   = yyyymmdd   or 20210126

#VARIABLES 
linebreak = "-" * 35
current_date = datetime.datetime.now()
current_time = datetime.datetime.now()
#   %b = Jan
#   %d = day of month numeric
Converted_Date = current_date.strftime("%A %d, %Y")
timeStamp = current_date.strftime("%Y%m%d")  # 20210126
#print("filename_" + timeStamp + ".txt")
#print("Start:" ,current_time)
#print("Today's Date:" ,current_date)
#print("month ", current_time.month)

print("Start Date:",current_date)  
print(linebreak)

#newdate = current_date + datetime.timedelta(days = 1000, hours=-1)
#print("New Date", newdate)

strName = 'James Bond'
strID = '007'
intHired = 1953
#print("Character name {0} ID: {1}, Hired {2}".format(strName, strID, intHired))
intNum = 1234567890
#print(intNum)
#print('{:,}'.format(intNum))

pi = 3.1415926
#print(pi)
#print('{:.4f}'.format(pi))


questions = 40
correct_answers = 23
#print(f"You got {correct_answers / questions :.2%} correct!")


fh = open("c:/ps1_files/mydemo.txt","r")
print(fh.readlines)
fh.close

# did my code run
print("\n" + linebreak)
print("Program Completed:",current_date)

