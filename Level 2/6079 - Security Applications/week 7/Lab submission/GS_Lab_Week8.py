#   NAME      [Gihan Shamike Liyanage]
#   id        [1142109]
#   FUNCTION  lab 7 example of CLASS, Ecapsulation
#   date      Fall 2022
#   ======================================

class student: 
    '''
    Create a constructor takes in student name - first name and Last name.
    Save them name into two instance Variables, one for first name and the '
    Last name. Variables should be private. 
    method that creates student ID and only public method should return the 
    user info. 
    '''
    __id_numbers = []  # private class variable to hold student IDs
    
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = self.__create_student_id()

    def __create_student_id(self):
        initials = self.__first_name[0].upper() + self.__last_name[0].upper()
        order_number = len(student.__id_numbers) + 1
        student_id = f"{initials}{order_number}"
        student.__id_numbers.append(student_id)
        return student_id

    def user_info(self):
        return f"Full Name: {self.__first_name} {self.__last_name}"
  

#Class that holds information on the program
class program:
    '''
    Create a constructor takes in program name and save it as a Instance Variable.
    Create two lists as instance Variables. One for course lists and students. 
    All ivariables should be private.
    
    Create 5 other methods. 
       * return the program name, 
       * another should allows to add a course, 
       * returns the course list, 
       * adds a student to program
       * returns student list
    '''
    def __init__(self, program_name):
        self.__program_name = program_name
        self.__course_list = []
        self.__student_list = []

    def add_course(self, course_name):
        self.__course_list.append(course_name)

    def get_program_name(self):
        return self.__program_name

    def get_course_list(self):
        return self.__course_list

    def add_student(self, student):
        self.__student_list.append(student)

    def get_student_list(self):
        return [student.user_info() for student in self.__student_list]


'''
Create an objects for each class.

when calling adding student to program use information from
student object

**** output should be****
ISM has 1 students

Student List:
Stav Aha
'''

# Create a Program object
ism_program = program("ISM")

# Add a course to the program
ism_program.add_course("Python")

# Create a Student object
student1 = student("Gihan", "Liyanage")
#student2 = student("John", "Cena")

# Add the student to the program
ism_program.add_student(student1)
#ism_program.add_student(student2)

print(ism_program.get_program_name(), "has", len(ism_program.get_student_list()), "students")

# Print the student list of the program
print("Student List:")
for student in ism_program.get_student_list():
    print(student)

# Print the course list of the program
print("Course List:", ism_program.get_course_list())