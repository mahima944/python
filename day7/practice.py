from abc import ABC,abstractmethod
class Vehicle:
    
    def __init__(self,brand):
        self.brand=brand
        @abstractmethod
        def max_speed(self):
            print pass
class car(Vehicle):
    def max_speed(self):
        print("200 km/h")
        
        
class bike(Vehicle):
    def max_speed(self):
        print("150 km/h")
        
c=car()
c.max_speed
b=bike()
b.max_speed

        
