# =========================================================
#	NAME:		GIHAN SHAMIKE LIYANAGE (1142109)
#	DATE:		SUMMER WEEK 9 2023
#	Function	Lab 8 Code Solution
#			Python 3.11.3
#			WING Personal 9
# =========================================================


# ===================== #
#	Part 2
# ===================== #

class X(object): 
    
    def __init__(self, a):
        self.num = a 

    def doubleup(self): 
        self.num *= 2

class Y(X): 
    
    def _init_(self, a): 
        X.__init__(self, a) 

    def tripleup(self): 
        self.num *= 3


print("============ Part 2 ============\n")       
y = Y(3)
print(y.num)  # Output: 3

y.tripleup()
print(y.num)  # Output: 9

y.tripleup()
print(y.num)  # Output: 27


# ===================== #
#	Part 3
# ===================== #

# Base or Super class 
class Person(object): 
    
    def __init__(self, name): 
        self.name = name 

    def getName(self): 
        return self.name 

    def isEmployee(self): 
        return False

# Inherited or Subclass (Note Person in bracket) 
class Employee(Person): 
    
    def __init__(self, name, eid): 
        super(Employee, self).__init__(name) 
        self.empID = eid 

    def isEmployee(sefl): 
        return True

    def getID(self): 
        return self.empID
    
    
print("\n============ Part 3 ============\n")
emp = Employee("geek1", "E101")
output = (emp.getName(), emp.isEmployee(), emp.getID())
print(output)


# ===================== #
#	Part 4
# ===================== #

import math

class Shape:

    def __init__(self, color='black', filled=False):
        self.__color = color
        self.__filled = filled

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled


class Rectangle(Shape):

    def __init__(self, length, breadth):
        super().__init__()
        self.__length = length
        self.__breadth = breadth

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_breadth(self):
        return self.__breadth

    def set_breadth(self, breadth):
        self.__breadth = breadth

    def get_area(self):
        return self.__length * self.__breadth

    def get_perimeter(self):
        return 2 * (self.__length + self.__breadth)


class Circle(Shape):
    
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.__radius


print("\n============ Part 4 ============\n")  

r1 = Rectangle(10.5, 2.5)

print("Area of rectangle r1:", r1.get_area())
print("Perimeter of rectangle r1:", r1.get_perimeter())
print("Color of rectangle r1:", r1.get_color())
print("Is rectangle r1 filled ?", r1.get_filled())
r1.set_filled(True)
print("Is rectangle r1 filled ?", r1.get_filled())
r1.set_color("orange")
print("Color of rectangle r1:", r1.get_color())

c1 = Circle(12)

print("\nArea of circle c1:", format(c1.get_area(), "0.2f"))
print("Perimeter of circle c1:", format(c1.get_perimeter(), "0.2f"))
print("Color of circle c1:", c1.get_color())
print("Is circle c1 filled ?", c1.get_filled())
c1.set_filled(True)
print("Is circle c1 filled ?", c1.get_filled())
c1.set_color("blue")
print("Color of circle c1:", c1.get_color())
