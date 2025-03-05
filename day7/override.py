from abc import ABC, abstractmethod  

class Father(ABC):  
    @abstractmethod
    def set_pan_details(self, pan_number):  # Abstract method for PAN details
        pass

    def show(self):  # Concrete method
        print("This is a concrete method of Father.")
        
class Son(Father):  
    def set_pan_details(self, pan_number):  # Overriding the abstract method
        self.pan_number = pan_number
        print(f"Son's PAN details set: {self.pan_number}")

class Daughter(Father):  
    def set_pan_details(self, pan_number):  # Overriding the abstract method
        self.pan_number = pan_number
        print(f"Daughter's PAN details set: {self.pan_number}")

# Instantiate and test  
s = Son()
s.set_pan_details("ABCDE1234F")  # ✅ Output: Son's PAN details set: ABCDE1234F
s.show()  # ✅ Output: This is a concrete method of Father.

d = Daughter()
d.set_pan_details("WXYZ5678G")  # ✅ Output: Daughter's PAN details set: WXYZ5678G
d.show()  # ✅ Output: This is a concrete method of Father.
