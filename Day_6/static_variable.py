class Animal:
    Animal_sound = "meow"  
    def __init__(self, sound):
        self.sound = sound  # Instance variable

    def make_sound(self):
        return self.sound  

p = Animal("bark")  
print(p.Animal_sound)  
print(Animal.Animal_sound)  
print(p.make_sound())  # Calling instance method


class Business():
    Business_name="art_craft"
    def  __init__(self,prons):
        self.prons= prons
        
    def make_prons(self):
        return self.prons
    
pros= Business("sketch painting")
print(pros.Business_name)
print(Business.Business_name)
print(pros.make_prons())
