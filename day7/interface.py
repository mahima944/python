from abc import ABC, abstractmethod
class parent(ABC):
    @abstractmethod
    def display(self):
        pass
    def display(self):
        print("This is a parent class")
        
class child(parent):
    
    def display(self):
        print("This is child class")
        
class grandchild(child):
    def display(self):
        print("This is grandchild class")

obj = grandchild()
obj.display()
obj1 = child()
obj1.display()
obj2 = parent()
obj2.display()



