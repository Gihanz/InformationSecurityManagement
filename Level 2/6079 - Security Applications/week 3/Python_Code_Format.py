#  FUNCTION     Week 3
#  DATE         MAY 2020 
#  DESCRIPTION  6079 Formatting, Dates
#      Dates 
#      Datetime module
#      String formatting
#      files 
#  ---------------------------------------------

import datetime
# here is where we set the initial variables for dates
datDate1 = datetime.datetime.now()
datDate2 = datetime.datetime.now().date()

# set up for current date
Current_time = datetime.datetime.now()
#print it out!!!
print("Current Date",Current_time)

#prints the default output
print("1st date:",datDate1) 
print("2nd date:",datDate2)

# option 1
datCurrent = datetime.datetime.now().date()
print("Option 1:", datCurrent)
# option 2
Current_date2 = datetime.date.today()
print("Current Date ", Current_date2)

'''
customizing print of date using options.
The options can be used in any order that you want or 
as often as you want.
You can also write what you want between the options

note the font case being used 
i.e. %a for abbreviated name of day
            Sun for Sunday
     %A for full name of day
            Sunday
there are other variable(Upper and Lower cases) than mean
different things!!!!   say %m = month number %M=minutes
something to memorize in your spare time
'''
# using the function(method) strftime - do some formatting
print(date.strftime("%b %d,%Y %H:%M:%S")) 
print(date2.strftime("Today is %d of %B in %Y"))

''' can split the output using some function calls from date
{} is used to reference the data following the .format statement 
      date.day = {0}, date.month = {1} and so on
NOW FORMAT THE OUTPUT - SEE HOW IS NOW NOW FORMATTED AND EASIER TO DTERMINE THE VALUES
'''
print("day:{0} month:{1} year:{2} hour:{3} minutes:{4} second: {5} microseconds: {6}".format(datDate1.day,datDate1.month,datDate1.year,datDate1.hour, datDate1.minute, datDate1.second, datDate1.microsecond))

#can split the output using some function calls from date2
# SEE HOW THE {} MATCHES THE VARIABLE LAYOUT IN THE FORMAT !!!
print("day:{0} month:{1} year:{2}".format(datDate2.day,datDate2.month,datDate2.year))

# Other ways to make it easier to read - just using str as they are not used for anything but output
# we can also get all the information you could want to know about time
strMonth = datDate2.month
strDay = datDate2.day
strYear = datDate2.year
# now just use reference variables
print("day:{0} month:{1} year:{2}".format(strDay,strMonth,strYear))

# SO AS WE CAN SEE - WE CAN SET THE DATE THEN GET ALL THE INFO USING .PROPERTIES OF THE OBJECT
# --------------------------------------------------------------------

# timedelta METHOD >>  an object that represents the difference between two dates
# see slides 14, 15, 16
# adding 1000 days
# obviously when coding - REVIEW the error messages and adjust accordingly
# datDate2 = it's current date plus adding the 1000 days in the datetime.timedelta method
date2 = date + datetime.timedelta(days = 1000)
print("NEW DATE = ",date2.strftime("%d/%m/%Y"))
'''
adding days or subtracting days is the main function you would be looking at
'''

# other uses of the timedelta method - you can also work with hours etc
# adding a year, 365 days, minus 1 hour
print(date.strftime("%d/%m/%Y %H:%M:%S"))

date2 = date + datetime.timedelta(days = 365, hours= -1)
print(date2.strftime("%d/%m/%Y %H:%M:%S"))



'''
String formatting code from here
'''

# initialize variables 
strFullName = "James Bond"
strID= "007"                # looked as a string to easily have leading 0's
strYearCreated = 1953
# make sure variables are consistent   <<<<  ###### NOTE  ######
print("Character name", strFullName,"ID:",strID,"Year Created:",strYearCreated)
# print out using references
print("Character name {0} ID: {1} Year Created: {2}".format(strFullName, strID, strYearCreated))
# print out - alternate format - look how referencing us changed
print("{0} was created in {2} and was given ID number: {1}".format(strFullName, strID, strYearCreated))

# print variables using text not #'s
# name, day
print("Course name: {strname} is on {strday}".format(strname = 'INFO 6079 Python Security', strday = 'Wednesdays'))


# FORMATTIN NUMBERS
# Formatting 1234567890 to 1,234,567,890 then adding a comment
print('New format {:,}'.format(1234567890))

# let's see what the following format is
# adds some spacing for readability
print('1: number:{:4d}'.format(42))
# no spacing
print('2: number:{0}'.format(42))


# formatting for decimals
pi = 3.1415926
print('{:3.2f}'.format(pi))
# {:   = formatting type
# 3    = round to 3 characters
# .2   = 2 decimals
# f    = format FLOAT
# as there is only 1 variable - handles by default!!
# same for FLOAT number 0 decimals so ROUNDS UP
myfloat = 2.71828
print("{:.0f}".format(myfloat))

# FILES
# FOR open()   see slides 29 - 38
# also review the notes that are also added to the presentation itself!!!
# this is also a review of WEEK 7