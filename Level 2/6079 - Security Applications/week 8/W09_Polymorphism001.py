#-----------------------------------
#  Author:    Me
#  Date       March 2020
#  Function:  Week 9 Polymorphism
#-----------------------------------

from datetime import date
#datDate = datetime.datetime.now()
datDate = date.today()

import random

class Car:
    def __init__(self, name):
        self.name = name
    
    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def stop(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Sportscar(Car):
    def drive(self):
        return 'Sportscar driving!'

    def stop(self):
        return 'Sportscar braking!'
    
class Truck(Car):
    def drive(self):
        return 'Truck driving slowly because heavily loaded.'

    def stop(self):
        return 'Truck braking!'

