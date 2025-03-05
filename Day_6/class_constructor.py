class Animal:
    def __init__(self, sound):
        self.sound = sound
    
    def make_sound(self):
        print(self.sound)
        
class cat(Animal):
    def __init__(self):
        super().__init__("meow")
    
class dog(Animal):
    def __init__(self):
        super().__init__("bark")
        
for animal in [cat(), dog()]:
    animal.make_sound()


class Books:
    def __init__(self, read):
        self.read= read
        
    def make_read(self):
        print(self.read)
        
class short_Book(Books):
    def __init__(self):
        super().__init__("read short books")
        
class long_Book(Books):
    def __init__(self):
        super().__init__("read long books")
        
for book in [short_Book(), long_Book()]:
    book.make_read()