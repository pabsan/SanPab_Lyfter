class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value
    
    def promote(self, percentage):
        if percentage < 0:
            raise ValueError("Percentage must be a positive value.")
        self._salary += (self._salary * percentage / 100)
    
    def print_info(self):
        print(f"Employee Name: {self._name}, Salary: {self._salary}")


employee = Employee("Ana", 1000)
employee.print_info()  # Employee Name: Ana, Salary: 1000
employee.promote(0.1)  # +10%
employee.print_info()  # Employee Name: Ana, Salary: 1100

try:
    employee.salary = -500  # This should raise a ValueError
except ValueError as e:
    print(e)  # Salary cannot be negative.

try:
    employee2 = Employee("Luis", -2000)  # This should also raise a ValueError
except ValueError as e:
    print(e)  # Salary cannot be negative.
