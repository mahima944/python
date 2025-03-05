class Bird:
    def __init__ (self,eat="seeds"):
        self.eat=eat   
    
    def fly(self):
        return "This bird can fly"
    
    def swim(self):
        return "bird can swim"
    
    def get_eat(self):
        return f"This bird eats {self.eat}"
    
class Mamal:
    def __init__(self, speed="fast"):
        self.speed=speed
    def walk(self):
        return "The mamal can walk"
    def run(self):
        return "The mamal can run"
    def get_speed(self):
        return f"The mamal runs {self.speed}"
    
class Bat(Bird,Mamal):
    def __init__(self, eat="fruits"):
        super().__init__(eat)
        
    def dance(self):
        return"kuchipudi"

bat = Bat()
print(bat.fly())
print(bat.walk())
print(bat.dance())

m1=Mamal()
m1=bat
print(m1.dance())