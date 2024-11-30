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

# Imports
import connect_DB

# Create VARIABLES

# Create Functions

# ACTUAL DO THINGS

'''
****Use only if database has been deleted**** 
Creates a file named logins.db that contains table called users.
Module also adds a user 'Admin' with password 'Admin' and role of 'admin'.
This user will serve as default admin user. 
'''
def create_DB():
    return Connect_DB.create()
    

def Check_user(user, password):
    db_result = connect_DB.check_for_user(user)
    
    if db_result == None:
        return [False] # return a list with one element 
    else:
        if db_result[1] != password:
            return [False] # return a list with one element 
    return [True, db_result[2]] # return a list with two element, True and role 

def add_user(username, password, role):
    '''
    make proper checks, could be put in __IsPasswordValid(password)
    1) Can not have two users in with same username. 
    2) password of proper length ... affecting new users only
    3) no one can put admin as their role
    CALL >> def update_users(e_user,e_password, e_role):
    '''
    isRoleValid = __IsRoleValid(role)
    isUsernameValid = __IsUsernameValid(username)
    isPasswordValid = __IsPasswordValid(password)
    
    if isRoleValid[0] == True:
    
        if isUsernameValid[0] == True:
            if isPasswordValid[0] == True:
                connect_DB.update_users(username, password, role)
                message = "User added successfully"
                send = [True, message]
            else:
                send = [False, isPasswordValid[1]] 
        else:
            send = [False, isUsernameValid[1]]
        
    else:
        send = [False, isRoleValid[1]]
        
    return send

def get_user_table():
    all_users = connect_DB.read_all_users()
    return all_users
 

'''
optional use   
could use this as a function that check if password meet requirements
could be used if you want to allow users to change their passwords
'''
def __IsPasswordValid(password): # method not seen in modules that import them. But, developer knows about function could call it
    has_lower = False
    has_upper = False
    has_number = False    
    
    if len(password) >= 8 and len(password) <= 30:
        
        # Check for numbers, lower and upper letters
        for char in password:
            if char.islower():
                has_lower = True
            if char.isupper():
                has_upper = True
            if char.isdigit():
                has_number = True  
                
        if has_lower and has_upper and has_number:             
            message = "Valid password"
            send = [True, message]
        else:
            message = "Password must contain numbers, lower and upper letters"
            send = [False, message]            
    else:
        message = "Password is too short"
        send = [False, message]
        
    return send

def __IsUsernameValid(user): # check username is available to use
    db_result = connect_DB.check_for_user(user)
    
    if db_result == None:
        message = "Valid"
        send = [True, message]
    else:
        message = "Username unavailable"
        send = [False, message]        
    
    return send

def __IsRoleValid(role): # check role is equal to Admin
    
    if role == "Admin" or role == "admin":
        message = "Invalid role"
        send = [False, message]
    else:
        message = "Valid"
        send = [True, message]        
    
    return send