

class car:
    def __init__(self,brand,car):
        self.brand=brand
        self.car=car
    def display(self):
        print(f"car is {self.brand}, {self.car}")

class employee:
    __allowance=1000
    def __init__(self,name,salary=10000):
        self.__private_name=name
        self.__private_salary=salary
    def set_salary(self,salary):
        self.__private_salary=salary
        return salary
    def get_salary(self):
        return self.__private_salary
    def salary_after_deduction(self):
        total_salary=self.__private_salary + self.__allowance
        return total_salary-total_salary*0.2
    def set_allowance(self,allowance):
        self.__allowance=allowance
        return allowance
    def get_allowance(self):
        return self.__allowance

class Parent:
    def __init__(self):
        self.bignose='5cm'
    def display_parent(self):
        print("this is parent class")
class child(Parent):
    def __init__(self,name,age):
        super().__init__()
        self.name=name  
        self.age=age    
    def display_child(self):
        print("this is the child class")

class student:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def display(self):
        print(f"student name is {self.name} and address is {self.address}")
class school(student):
    def __init__(self,name,address,school):
        super().__init__(name,address)
        self.school=school
    def display_school(self):
        print(f"school name is {self.school}")
class college(student):
    def __init__(self,name,address,college):
        super().__init__(name,address)
        self.college=college


temp=college("sai","hyd","jntu")
temp.display()
