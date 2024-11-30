#  ---------------------------------------------
#  AUTHOR       Bruce Hansen
#  FUNCTION     Week 3 Lecture
#  DATE         MAY 2021
#  DESCRIPTION  Info 6079

#  ----------------------------------
#  IMPORT MODULES
import datetime as DT

# ----------------------------------
# SETING MY VARIABLES
strBreakLine = "-" * 25
datDateTime = DT.datetime.now()
datDate = DT.datetime.now().date()
#print("date and time " ,datDateTime)
print("Program")
print("Current Date", datDate)
print(strBreakLine)
#xYear = datDateTime.year
#xMonth = datDateTime.month

strName = "James Bond"
strID= "007"
lngCreated = 1953

xdate = datDateTime.strftime("%b %d, %Y")
#print("Date is", xdate)
#print(strBreakLine)
#print("year =" , xYear)
#print("month =", xMonth)

# SET UP FUNCTIONS

# NOW DO STUFF
newdate =  datDateTime + DT.timedelta( weeks = 104 )
#print("new date", newdate)

#print a string of variables
#print("Character name", strName,"ID:",strID,"Year Created:",lngCreated)
#print("ID {1} Joined:{2} Agent Name {0} ".format(strName, strID, lngCreated))
#print("Course name: {course} is on {day}".format(course='INFO-6079 Python Security', day='Tuesdays'))
print("formatting numbers")
#print('{:,}'.format(1234567890))

pi = 3.1415926
#print('PI is now {:.4f}'.format(pi))

myfloat = 2.71828
#print('myFloat is {:.1f}'.format(myfloat*7 ))
'''
questions = 50
correct_answers = int(input("Enter Answers Correct: "))
print(f"You got {correct_answers / questions :.2%} correct!")
'''

fh = open('c:\py_files\Week3_hello.txt', 'w')
lines_of_text = ["a line of text\n", "another line of text\n", "a third line\n"]
fh.writelines(lines_of_text)
fh.close()

fh = open("c:\py_files\Week3_hello.txt", "a")
fh.write(str(xdate))
fh.write("\n>> Hello World again")
fh.close()


# ALL DONE
print("\n"+strBreakLine)
print("COMPLETED")
print(datDateTime)
