from abc import ABC,abstractmethod
class Father(ABC):
    
    @abstractmethod
    def disp(self):
        pass
    
f=Father()

class child(Father):
    def disp(self):
        print("This is child class")
        
class child1(Father):
    def disp(self):
        print("This is child1 class")
        
c=child()
c.disp()
c1=child1()
c1.disp()