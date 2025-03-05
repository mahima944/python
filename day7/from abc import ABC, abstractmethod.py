from abc import ABC, abstractmethod

# Interface definition: This class will define the interface for setting and displaying PAN details
class PANCardDetailsInterface(ABC):
    
    @abstractmethod
    def set_pan_details(self, pan_number):  # Abstract method to set PAN details
        pass

    @abstractmethod
    def display_pan_details(self):  # Abstract method to display PAN details
        pass

# Father class implementing the interface
class Father(PANCardDetailsInterface):
    
    def __init__(self):
        self.pan_number = None
    
    def set_pan_details(self, pan_number):  # Implementing abstract method
        self.pan_number = pan_number
        print(f"Father's PAN details set: {self.pan_number}")
    
    def display_pan_details(self):  # Implementing abstract method
        print(f"Father's PAN Number: {self.pan_number}")

# Son class inheriting from Father and overriding methods
class Son(Father):
    
    def set_pan_details(self, pan_number):  # Overriding the method
        self.pan_number = pan_number
        print(f"Son's PAN details set: {self.pan_number}")
    
    def display_pan_details(self):  # Overriding the method
        print(f"Son's PAN Number: {self.pan_number}")

# Daughter class inheriting from Father and overriding methods
class Daughter(Father):
    
    def set_pan_details(self, pan_number):  # Overriding the method
        self.pan_number = pan_number
        print(f"Daughter's PAN details set: {self.pan_number}")
    
    def display_pan_details(self):  # Overriding the method
        print(f"Daughter's PAN Number: {self.pan_number}")

# Testing the implementation
father = Father()
father.set_pan_details("ABCDE1234F")
father.display_pan_details()

son = Son()
son.set_pan_details("FGHI5678J")
son.display_pan_details()

daughter = Daughter()
daughter.set_pan_details("JKLM9876K")
daughter.display_pan_details()
