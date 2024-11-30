#parent class
class Employee(): 
    
    def __init__(self, Fname, Lname, role):   # Method
        self.fname = Fname   # First Instance Variables
        self.lname = Lname   # Second Instance Variables
        self.role = role   
        self.__set_email()
        self.__salary_cal()
    
    def print_Employee_info(self):
        print("{0} {1}, the {2}, email is: {3}".format(self.fname, self.lname, self.role, self.email))
        print("Salary:", self.salary)
    
    def __set_email(self): 
        self.email = self.fname + self.lname + "@company.ca"
        
    def __salary_cal(self):
        self.salary = 50000
        
        if self.role == "Manager":
            self.salary += 30000
    
    def get_salary(self):
        return self.salary
    

#child class
class Clevel(Employee):  
    def __init__(self, Fname, Lname, role):   # Method
        role = "CEO"
        super().__init__(Fname,Lname, role)
        self.__salary_cal()

    def __salary_cal(self):
        self.salary = 100000
        
        if self.role == "CEO":
            self.salary = 130000
            
#child class
class Manager(Employee):
    #once called self.budget variable is created
    def set_budget(self, num_Employees):
        self.budget = num_Employees * 2000 

E1 = Employee("Dave", "Lee", "Customer service") #creating Employee Object
E2 = Manager("John", "Smith", "Manager") # creating Manger Object
E3 = Clevel("Jane", "smith", "CEO") # creating CLevel object 
E4 = Clevel("Stav", "Aha", "CTO") # creating CLevel object

'''
print("{0} {1}'s has title of {2} with salary of {3} and can be reached at {4}".format(E1.fname, E1.lname,E1.role, E1.salary, E1.email))
print("{0} {1}'s has title of {2} with salary of {3} and can be reached at {4}".format(E2.fname, E2.lname,E2.role, E2.salary, E2.email))
print("{0} {1}'s has budget of {2}".format(E2.fname, E2.lname, E2.budget)) # need to uncomment line 49
print("{0} {1}'s has title of {2} with salary of {3} and can be reached at {4}".format(E3.fname, E3.lname,E3.role, E3.salary, E3.email))
'''


EmployeesL= [E1,E2,E3,E4] 
print("Company employees")

for em in EmployeesL:
    print(em.fname, em.lname)
    print(em.email)
    print(em.role)
    print(em.get_salary())
    if em.role == "Manager":
        em.set_budget(5)
    print("------")
    



