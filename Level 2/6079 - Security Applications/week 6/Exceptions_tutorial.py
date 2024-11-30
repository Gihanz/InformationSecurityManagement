# Function      Info6079 Lab 6 week 7 
#               Exceptions
# Date          F2022
# Python        3.10.7
# ------------------------------------

import sys

randomlist = ['a', 0, 2]

for x in randomlist:
    try:
        print("list item is",x)
        r = 1/int(x)
        break
    except:
        print("oops!",sys.exc_info()[0],"occurred")
        print("next entry")
        print("")
        
print("the reciprocal of",x ,"is",r)