# ---------------------------------------
# AUTHOR   Bruce Hansen
#          Week 8 Classes
#          June 2021
# ---------------------------------------
import datetime

# VARIABLES  ----------------------------
datToday = datetime.datetime.now().date()
datNow = datetime.datetime.now()
strLineBreak = 25 * "-"

#CLASSES
class clAUTO:
    def __init__(self, strMFG, strEngine, strModel, strType):
        self.mfg = strMFG       # Toyota, Honda, Ford
        self.engine = strEngine # size
        self.model = strModel   # Civic, Rav4 etc.
        self.xType = strType    # SUV, sedan, truck
    
    def fnShowMFG_Model(self):
        # Date:      March 7, 2022
        # Function : displays the MFG Model
        print("MFG model {0} - {1}".format(self.mfg,self.model))
        
    def fnShowFull_Auto(self):
        # Date:      March 7, 2022
        # print full description of auto entered
        print("Auto: {0} \t {1} \t{2} \t {3}".format(self.mfg,self.model,self.engine, self.xType))
        
         
auto001 = clAUTO("Toyota", "1600cc", "Rav4", "2dr sedan")
auto002 = clAUTO("Honda","1698", "Civic","4dr sedan")
auto003 = clAUTO("Ford", "8 cyl","F150","extTruck")

AutoList = [auto001, auto002, auto003]

for ao in AutoList:
    ao.fnShowFull_Auto()

print("\n",strLineBreak)
print("Added OK")