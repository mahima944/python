from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius= radius
        
    def area(self):
        return 3.14*(self.radius**2) 
    def perimeter(self):
        return 2*3.14*self.radius  
    
class rectangle(shape):
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
        
    def area(self):
        return self.length*self.breath
    def perimeter(self):
        return 2*(self.length+self.breath)
    
c=circle(7)
print(f"Area of circle{c.area()} and perimeter is:{c.perimeter()}")
r=rectangle(4,5)
print(f"Area of rectangle{r.rectangle()} and perimeter is {c.perimeter()}")
