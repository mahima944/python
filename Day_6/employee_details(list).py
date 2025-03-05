class Employee:
    def __init__(self, name, salary, emp_id):
        self._name = name
        self._salary = salary
        self._id = emp_id

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def get_id(self):
        return self._id

# Create a list to store Employee objects
employees_list = []

# Take input for one employee
details = input("Enter name, salary, id separated by commas: ").split(',')
name = details[0]
salary = float(details[1])
emp_id = int(details[2])

# Create the Employee object and add it to the list
employee_obj = Employee(name, salary, emp_id)
employees_list.append(employee_obj)

# Print the details of the employee in the list
print("The details of the employee:")
for emp in employees_list:
    print(f"Name: {emp.get_name()}, Salary: {emp.get_salary()}, ID: {emp.get_id()}")
