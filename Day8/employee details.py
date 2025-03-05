from abc import ABC, abstractmethod
from typing import List

# Step 1: Define Employee interface using Abstract Base Class (ABC)
class Employee(ABC):
    @abstractmethod
    def work(self) -> str:
        pass
    
    @abstractmethod
    def get_salary(self) -> float:
        pass
    
    @abstractmethod
    def promote(self) -> str:
        pass

# Step 2: Create concrete classes for different types of employees
class Manager(Employee):
    def __init__(self, name: str, salary: float, role: str = "Manager"):
        self.name = name
        self.salary = salary
        self.role = role
    def work(self) -> str:
        return f"{self.name} is managing the team as a{self.role}."
    
    def get_salary(self) -> float:
        return self.salary
    
    def promote(self) -> str:
        self.role = "senior manager"
        self.salary*=1.2 
        print(f"{self.name} has been promoted! New role: {self.role}, New salary: {self.salary}")   

class Developer(Employee):
    def __init__(self, name: str, salary: float, role: str = "Developer"):
        self.name = name
        self.salary = salary
        self.role = role
    def work(self) -> str:
        return f"{self.name} is working as a {self.role}."
    
    def get_salary(self) -> float:
        return self.salary
    
    def promote(self) -> str:
        self.role= "senior Developer"
        self.salary*=1.2
        print(f"{self.name} has been promoted! New role: {self.role}, New salary: {self.salary}")

class Intern(Employee):
    def __init__(self, name: str, salary: float, role: str="Intern"):
        self.name = name
        self.salary = salary
        self.role = role
    
    def work(self) -> str:
        return f"{self.name} is learning and assisting."
    
    def get_salary(self) -> float:
        return self.salary
    
    def promote(self) -> str:
        self.role="junior Developer"
        self.salary*=1.2
        print(f"{self.name} has been promoted! New role: {self.role} New salary: {self.salary}")

class Security(Employee):
    def __init__(self, name: str, salary: float, role:str="security"):
        self.name = name
        self.salary = salary
        self.role=role
    
    def work(self) -> str:
        return f"{self.name} is securing the assets."
    
    def get_salary(self) -> float:
        return self.salary
    
    def promote(self) -> str:
        self.role = "senior security"
        self.salary*=1.2
        print(f"{self.name} has been promoted! New role: {self.role} New salary: {self.salary}")

# Step 3: Define Department class that manages Employees
class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees: List[Employee] = []
    
    def hire(self, employee: Employee) -> None:
        self.employees.append(employee)
        print(f"{employee.name} has been hired.")
    
    def fire(self, employee: Employee) -> None:
        self.employees.remove(employee)
        print(f"{employee.name} has been fired.")
    
    def promote(self, employee: Employee) -> None:
        if employee in self.employees:
            employee.promote()
        else:
            print(f"{employee.name} is not in this department.")
    
    def get_total_salary(self) -> float:
        return sum(employee.get_salary() for employee in self.employees)
    
    def show_employee_details(self) -> None:
        print(f"Employees in {self.name} Department:")
        for employee in self.employees:
            print(f"- {employee.name}, Salary: {employee.get_salary()}, Role: {employee.work()}")

# Step 4: Create department and add employees
# Create employees
manager = Manager("Alice", 80000)
developer = Developer("Bob", 60000)
intern = Intern("Charlie", 20000)
security_staff = Security("Ram", 5000)

# Create a department and hire employees
it_department = Department("IT")
it_department.hire(manager)
it_department.hire(developer)
it_department.hire(intern)
it_department.hire(security_staff)

# Show employee details before promotion
it_department.show_employee_details()

# Promote an employee
it_department.promote(manager)

# Show employee details after promotion
it_department.show_employee_details()

# Total salary in the department
total_salary = it_department.get_total_salary()
print(f"Total salary expense for {it_department.name} department: ${total_salary}")
