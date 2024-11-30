print("Hello Word")

Test1 = 90.5
Test2 = 97
Test3 = 85.5

Course_average = (Test1 + Test2 + Test3)/3
print("Student average", Course_average)

print("11 divided by 3 is", 11/3)
print("-11 divided by 3 is", -11/3)

Age = int(input('Enter your age: '))
print("your age is" , Age)


import sys
print(sys.version)

message = 'Please wait while the program is loading...'
print(message)

def print_a(): 
    print ("a")
    
print_a()

def repeat_string(string, num):
    repeated_string = (string + ' ') * num
    return repeated_string

# example usage
print(repeat_string('hello', 3))  # output: 'hello hello hello'
print(repeat_string('abc', 5))  