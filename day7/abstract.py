from abc import ABC, abstractmethod  

class Father(ABC):  
    @abstractmethod
    def _disp(self):  
        pass

    def show(self):  # Concrete method
        print("Concrete method")
        
class son(Father):
    def _disp(self):
        print("son is implementing the abstract method")
        
class Daugther(Father):
    def _disp(self):
        print("Daugther is implementing the abstract method")
        
s = son()
s._disp()
s.show()

from abc import ABC, abstractmethod  

class Artist(ABC):  
    @abstractmethod
    def _disp(self): 
        pass

    def draw(self): 
        print("Drawing")

class Sketch(Artist): 
    def _disp(self):  
        print("Sketch is implementing the abstract method")

class Painting(Artist):  
    def _disp(self):  
        print("Painting is implementing the abstract method")


sk = Sketch()
sk._disp()  
sk.draw()
