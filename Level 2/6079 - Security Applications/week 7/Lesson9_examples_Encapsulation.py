class Employee:
    __num_of_Employees = 0 # Class variables that can only be reached from a Method
    
    def __init__(self, name, role):   # Method
        self.name = name   # First Instance Variables
        self.role = role   # Second Instance Variables
        self.__addEmployeeCount() 
    
    def print_Employee_info(self):
        print("{0} {1}".format(self.role, self.name))
    
    def __addEmployeeCount(self): # can only be reached from the class. 
        Employee.__num_of_Employees += 1 # Updates the class variable 
   
    def Employee_count(self): #everyone can print the value of the shared variable __num_of_Employees
        return int(Employee.__num_of_Employees) 
    

E1 = Employee("John Smith", "Manager") #creating object person
print("Company has",E1.Employee_count(), "employees.") #printing current number of employees

E2 = Employee("Jane Smith", "CEO") #creating object person
print("Company has",E1.Employee_count(), "employees.") #printing current number of employees

E3 = Employee("FName LName", "No Title") #creating object person
print("Company has",E1.Employee_count(), "employees.") #printing current number of employees

print() 
EmployeesL= [E1,E2,E3] 
print("Company employees")
for em in EmployeesL:
    em.print_Employee_info() #prints the people names




