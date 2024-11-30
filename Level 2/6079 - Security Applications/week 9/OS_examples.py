#!/usr/bin/env python3

import os
#Current Working Directory(CWD)
print("Current Working Directory(CWD)")
print(os.getcwd())
print()

#absolute path on your system
print("absolute path on your system")
print(os.path.abspath('.'))
print()

# To print files and directories in the current directory 
print("print files and directories in current Directory")
print(os.listdir()) 
print(os.listdir('.')) #same result of above line
print()

print("current directory ... printed via loop")
files = [f for f in os.listdir('.')]
for f in files:
    print(f)
print()

# To print files and directories in the directory located above current 
print("print files and directories in of directory above current one")
print(os.listdir('..'))
print()

# To print files and directories on your windows system 
path = 'c:\\'
print("print files and directories in", path)
print(os.listdir(path))
print()


'''
A function that lets you get using os.walk() get all files in a diractory,
including files in subfolders
'''
def get_files_in_Fold(path):
    num = len(path)
    if num == 0:
        path = "." #say to look at the same folder the Python file is located
    
    for root, dirs, files in os.walk(path):
        for file in files:
            print("{0}\{1}".format(root, file))
        
    

#get path from user
u_path = input("Enter a folder path: ")
print("Files in Folder")  
get_files_in_Fold(u_path)#calls function

print(os.environ)