# ------------------------------------
# NAME        Gihan Shamike Liyanage
# FUNCTION    Week 4  Lab 4
#             used in conjunction with Lab 
#             to provide logic to LAB 4 to connect to Database
#             created with sqlite3 module
# DATE        SUMMER 2023
# Python      3.11.3
#             WING Personal 9
# ------------------------------------

# Import Lab_week4_logic as logic 
import GS_Lab04_logic as logic
print(logic.connect_DB.create())

'''
Ask user to user if new user or existing? 
If new add new user and loopback to prompt, 
if existing check credintials.
if successful login and give options to Admin.
All other users just print logded and close application
'''
not_logged = True
count = 0

existing_user = input("Are you an existing user? [y,n] ") 
while not_logged:
    count +=1

    if existing_user == "y" or existing_user == "Y":
        username = input("Username: ")
        password = input("Password: ")

        is_user = logic.Check_user(username,password)
        if is_user[0]: # checks the first elemet of list is true 
            print("Hello ", username)
            if is_user[1] == "admin":
                users = logic.get_user_table()
                for user in users:
                    # print(user)
                    print("Username: {0}, Password: {1}, Role: {2}".format(user[0], user[1], user[2]))
                
            not_logged = False
            print()
            print("Logging out")
            
        else:
            print("Wrong credentials , try again")
            if count == 3: # gives 3 trys
                print("good bye")
                not_logged = False
    else:
        adding_user = True
        print("Welcome new user!!!")
        while adding_user:
            print()
            print("Please enter your information")
            username = input("Enter Username: ")
            password = input("Enter Password: ") 
            role = input("Enter Role: ") 
            print()
        
            result= logic.add_user(username,password,role) 
            print(result[1])
            adding_user = result[0]
               
        not_logged = False