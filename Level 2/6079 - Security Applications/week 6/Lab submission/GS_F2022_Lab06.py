# INFO-6079  Fall 2022 LAB 6  
#     Sockets
#     Exceptions

# =========================================================
# NAME:		GIHAN SHAMIKE LIYANAGE (1142109)
# DATE:		SUMMER WEEK 6 2023
# Function	Lab 6 Code Solution
#		Python 3.11.3
#		WING Personal 9
# =========================================================


# IMPORTS
import random

# VARIABLES

# Header information
header_file = "Game Results.txt"
header_info = "Name: Gihan Shamike Liyanage\nStudentNo: 1142192\nCourse: INFO6079\nDate: SUMMER WEEK 6 2023\n\n"

# LAB CODE WILL FOLLOW THE LAB STEPS

# create file
with open(header_file, "w") as h:
    
     # Write the header information
    h.writelines(header_info)
    
    print("I will generate a random number, and your task will be to make a guess for it...\n\n")

    # Generate a random number
    random_number = random.randint(1, 100)

    guess_count = 0
    max_guesses = 5
    
    while True:
        try:
            # Check if the maximum number of guesses has been exceeded
            if guess_count >= max_guesses:
                print("Maximum number of guesses exceeded!")
                h.writelines("Maximum number of guesses exceeded!\n")
                
                print("The random number is:", random_number)
                h.writelines("The random number is: {}\n".format(random_number))
                             
                break
    
            # Ask for a new number from the user
            user_number = int(input("Enter a number: "))
    
            # Check if the user's number matches the random number
            if user_number == random_number:
                print("Congratulations! You have guessed the correct number.")
                h.writelines("Congratulations! You have guessed the correct number.\n")
                
                print("The random number is:", random_number)
                h.writelines("The random number is: {}\n".format(random_number))
                
                break
            
            elif user_number > random_number:
                print(user_number,"is too high. Try again.")   
                h.writelines(str(user_number)+" is too high. Try again.\n")
            else:
                print(user_number,"is too low. Try again.")
                h.writelines(str(user_number)+" is too low. Try again.\n")
    
            guess_count += 1
    
        except ValueError:
            # Catch any errors in user input
            print("Invalid input. Please enter a number.")
            h.writelines("Invalid input. Please enter a number.\n")
            

# CODE END

    
