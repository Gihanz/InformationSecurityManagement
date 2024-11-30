#  FUNCTION     Week 3 code
#  AUTHOR       Bruce Hansen
#  DATE         January 2021
#  DESCRIPTION  Lesson 3 for Info 6079
#  REVISION     1.001
#      Dates 
#      Datetime module
#      String formatting
#      working with files 
#  ---------------------------------------------
# using the module: datetime
import datetime

# VARIABLES   ----------------------------------
current_time = datetime.datetime.now()
# print("Date/Time:" ,current_time)

datCurrent = datetime.date.today()
# print("Date :" , datCurrent)    # use as my log date
print("Lecture Week 3 code")
datToday = current_time.strftime("%b %d, %Y")
print("Today...", datToday)

#print("day is", current_time.day)
#print("mon is", current_time.month)
#print("year is", current_time.year)

spacer = " "            # just set  a variable to a space
underlineX = "-" * 25   # this is my underscore spacer line
# print(spacer)
print(underlineX)

# return 2 variables and the result of multiplying each
#def fnX(codeA, codeB, cadeC):
    #varResult = codeA * codeB * cadeC
    #return varResult

#x = fnX(75549,557,1)
# print("fnX returns", x)

# start coding  ---------------------
# DATE formats
#newdate = datCurrent + datetime.timedelta(weeks=52)
#print("newdate = ", newdate)

# STRING Formats
'''
strName = "James Bond"
strID = "007"
intYearHired = 1950
print("Spy:", strName, "ID:",strID, "hired:", intYearHired)
print("Agent {0}  ID {1}  Hired {2}".format(strName,strID,intYearHired))
'''

# NUMBERS
numX = 123456789
print("number with commas", "{:,}".format(numX))

pi = 3.1415926356354567
print("PI", '{:.2f}'.format(pi))

flNum = 23.789

print(flNum , "Floating is now rounded", '{:.1f}'.format(flNum))