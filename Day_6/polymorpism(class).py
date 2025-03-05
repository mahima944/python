class cat:
    def sound(self):
        print("Meow")
        
class Dog:
    def sound(self):
        print("bark")
        
for animal in [cat(),Dog()]:
    animal.sound()