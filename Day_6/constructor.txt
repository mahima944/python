class Car1:
    def __init__(self, name=None, mileage=None):
        if name:
            print(f"car name: {name}")
        if mileage:
            print(f"car mileage: {mileage}")
        
obj = Car1(mileage=25)  # Calls the constructor with mileage

class Example:
    def __init__(self, *args):
        if len(args) == 1:
            print(f"Hello {args[0]}")
        elif len(args) == 2:
            print(f"Hello {args[0]}, you are {args[1]} years old")

obj1 = Example("Alice")  # Calls the constructor with one argument

class Example2:
    def __init__(self, studentName, **kwargs):
        self.studentName = studentName
        if "name" in kwargs and "age" in kwargs:
            print(f"Hello {kwargs['name']}, you are {kwargs['age']} years old")
        elif "name" in kwargs:
            print(f"Hello {kwargs['name']}")
        if "name" in kwargs:
            self.inputname = kwargs['name']
        else:
            self.inputname = None

obj2 = Example2(studentName="John", name="mahi")
print("Elements in kwargs are:", obj2.inputname)
