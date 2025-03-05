from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
class dog(Animal):
    def make_sound(self):
        print("the dog barks")
        
class cat(Animal):
    def make_sound(self):
        print("the cat meows")
        
c=cat()
c.make_sound()
d=dog()
d.make_sound()
    