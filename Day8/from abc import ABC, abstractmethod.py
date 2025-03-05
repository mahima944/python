from abc import ABC, abstractmethod
from typing import List
class Employee(ABC):
    @abstractmethod
    def work(self):
        pass
    @abstractmethod
    def get_salary(self):
        pass
    
class Manager(Employee):
    def __init__(self,name,salary):
        self.name=name
        self,salary=salary
        
    def work(self):
        return f"{self.name} is managing"
    
    def get_salary(self):
        return f"{self.name} is getting salary of{self.salary}"
    
class Developer(Employee):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def work(self):
        return f"{self.name} is developing"
    
    def get_salary(self):
        return f"{self.name} is getting salary of{self.salary}"
    
    class Designer(Employee):
        def __init__(self,name,salary):
            self.name=name
            self.salary=salary
            
            def work(self):
                return f"self,name is designimg"
            
            def get_salry(self):
                return f"{self.name} is gettting salary of {self.salary}"
            
class Department:
    def __init__(self,name:str):
        self.name=name
        self.employees: List[Employee]=[]
        
    def hire(self,employee:Employee) ->None:
        self.employees.append(employee)
        print (f"{employee.name} has been hierd")
        
    def fire(self,employeee:Employee):
        self.employeesremove(employee)
    
        
        
        
        
        
    def get_all_salaries(self):
        return sum([employee.get_salary() for employee in self.employees])
        