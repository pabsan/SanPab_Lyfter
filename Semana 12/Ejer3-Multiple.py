#########################
# Ejemplo 1
class Phone:
    def call(self, number):
        print(f"Calling {number}...")
    

class Reproducer:
    def play_music(self, song):
        print(f"Playing song: {song}...")

class Navigation:
    def navigate_to(self, destination):
        print(f"Navigating to {destination}...")

class SmartPhone(Phone, Reproducer, Navigation):
    pass

#########################
# Ejemplo 2
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
class Employee:
    def __init__(self, id_number, position):
        self.id_number = id_number
        self.position = position

class Driver:
    def __init__(self, license_number):
        self.license_number = license_number

class EmployeeDriver(Person, Employee, Driver):
    def __init__(self, name, age, id_number, position, license_number):
        Person.__init__(self, name, age)
        Employee.__init__(self, id_number, position)
        Driver.__init__(self, license_number)


print("#############################")
print("# Ejemplo 1 ")
my_smartphone = SmartPhone()
my_smartphone.call("888-8888888") 
my_smartphone.play_music("John Lennon - Give Peace a Chance")
my_smartphone.navigate_to("Central Park, NY")

print("#############################")
print("# Ejemplo 2")
my_person = EmployeeDriver("Pablo", 43, "EMP123", "Driver", "401234567")
print(f"Employee Driver Info: Name: {my_person.name}, Age: {my_person.age}, ID: {my_person.id_number}, Position: {my_person.position}, License: {my_person.license_number}")
