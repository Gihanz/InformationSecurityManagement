'''
play with code to see how the file will change
get_file_data reads from file and save information in working_data so we can use the information
print_file_data just prints, no saving of data
write_to_file ereases file and saves string it gets to file
append_file adds a string to end of file
'''

file = "text.txt"
working_data = "" # data seen in python
#file could be replaced with a string "text.txt
#default mode is r

def get_file_data():
    with open(file,"r") as f: #got file from line 1
        print("At byte number:",f.tell()) #prints at which byte we start from 
        data_from_file = f.read() #data got from file
        print("At byte number:",f.tell()) #prints at which byte we end at
         
    print("Done, reading file!!!")
    print()
    return data_from_file # we are sending back the data we got from the file

def get_file_lines_in_list():
    line_list =[] 
    with open(file,"r") as f: #got file from line 1
        for line in f:
            line_wo_nline = line[:-1] #removing the \n at the end of the line
            line_list.append(line_wo_nline)
    return line_list
         

def print_file_data(): 
    with open(file,"r") as f: #got file from line 1
        print(f.read())
        

def write_to_file(data_to_file): #data_to_file is data we want to put in a file
    #w means write if the file exsits the information will be erast
    with open(file,"w") as f:
        f.write(data_to_file)
    
    print("Done writing")
    print()
    #there is no return, because we are saving information to file and not getting anything

def append_file(add_data): # we are adding information to end of file 
    with open(file,"a") as f:
        f.write(add_data)

    print("Done appending")
    print()
    


#start of program
working_data = get_file_data() #get_file_datawill fill working_data with information from the file in line 1

#now that working_data is filled we could work with it
print(working_data) #prints the information 

# adding data to working_data
#try playing with adding differant infromation and with \n.  \n says newline


file_lines = get_file_lines_in_list()
print("printing from list\n")
for i in file_lines:
    print(i)
print()


working_data += "Line 3 \n"


# lets say the information to the file
write_to_file(working_data)
print_file_data()

append_file("appended line \n")

print_file_data()



