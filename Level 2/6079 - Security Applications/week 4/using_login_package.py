# ------------------------------------
# FUNCTION    Week 4  Lab 4
#             used in conjunction with Lab 
#             to provide logic to LAB 4 
#             created with sqlite3 module
# DATE        FALL 2021
# Python      3.8 or 3.9.6
# ------------------------------------
import Login

username = input("Username: ")
password = input("Password: ")

u_result = Login.is_user_name(username)
p_result = Login.password.is_password(password)


if u_result and p_result:
    print("you are logged in")
else:
    print("failed to log in")
    
#print(Login.extra_code.random_information())
