# FUNCTION - SIMPLE TRY

try: 
    # Open file in read-only mode
        with open("hbh_lab6_output.txt", 'a') as f:
                f.write("\nHello World!")
        
except IOError as e:
    print("An IOerror occurred:", e)
    
print("done")

    