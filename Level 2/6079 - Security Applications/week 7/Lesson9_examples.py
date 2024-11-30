#   FILE                  Lesson9_examples.py
#   FUNCTION        example of CLASS
#   ======================================

#  ------------------------------------------
#  CLASS    mPhn      track phone information
class mPhn:
    num_of_phones = 0   
    def __init__(self, phnNumber, phnType, phnBattery, phnSize, phnXmit , phnModelNo):  # Method
        self.mphnModelNo= phnModelNo
        self.mphnNumber = phnNumber
        self.mphnType = phnType
        self.mphnbatteryType = phnBattery    # does it have a battery, type??
        self.mphnScreenSize = phnSize           # screen size
        self.mphnXmit = phnXmit                   # 3G , 4G, 5G   etc
        #self.mphnColour = phnColour            # colour of phone
        #self.mphnCameraPX = phnCameraPX   # pixel size of camera
        mPhn.num_of_phones += 1               # increment the variable count
     
    def print_Phone_info(self):
        print("{0} {1}".format(self.mphnNumber, self.mphnType))        
   
    
# PHN  start adding information
PHN1 = mPhn("567-6557","big","yes", "4in","5G", "XG5400")
print("phone # is", PHN1)
PHN2 = mPhn("547-5437","medium","yes", "6in","4G", "YT989")
print("phone # is", PHN2)
PHN3 = mPhn("676-098-0976","medium","yes", "5in","5G", "XD567U")
print("phone # is", PHN3)


#  ------------------------------------------
#  NEW CLASS    EMPLOYEE    track employee data
class Employee: 
    num_of_Employees = 0         # Class variables
    
    def __init__(self, name, role):    # Method
        self.name = name               # First Instance Variables
        self.role = role               # Second Instance Variables
        Employee.num_of_Employees +=1  # Updates the class variable 
    
    def print_Employee_info(self):
        print("{0} \t{1}".format(self.role, self.name))

print("Company has",Employee.num_of_Employees, "employees.") #printing 0 Employees, since there is no employees

E1 = Employee("John Smith", "Manager") #creating object person
print("Company has",Employee.num_of_Employees, "employees.") #printing 1 Employees, Since there is 1 employees

E2 = Employee("Jane Smith", "CEO") #creating object person
print("Company has",Employee.num_of_Employees, "employees.") #printing 2 Employees, Since there is 2 employees

E3 = Employee("FName LName", "No Title") #creating object person
print("Company has",Employee.num_of_Employees, "employees.") #printing 3 Employees, Since there is 3 employees

E4 = Employee("Robert Johnson", "Idol") #creating object person
print("Company has",Employee.num_of_Employees, "employees.")

print() 
EmployeesL= [E1,E2,E3, E4] 
print("Company employees")
for em in EmployeesL:
    em.print_Employee_info() #prints the people names
   
