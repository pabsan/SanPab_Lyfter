class Person:
    def __init__(self, name, age):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a string")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer")
        self.name = name
        self.age = age


class Bus:
    def __init__(self):
        self.capacity = 5
        self.passengers = []
    
    def board(self, person):
        if isinstance(person, Person) is False:
            raise ValueError("Only Person instances can board the bus")

        if len(self.passengers) < self.capacity:
            print(f"{person.name} boarded the bus with age {person.age}. Remaining capacity: {self.capacity}")
            self.passengers.append(person)
        else:
            print("Bus is full. Cannot board more passengers.")
    
    def unboard(self):
        if len(self.passengers) > 0:
            person = self.passengers.pop(0)
            print(f"{person.name} unboarded the bus with age {person.age}. Remaining capacity: {self.capacity - len(self.passengers)}")
        else:
            print("No passengers to unboard.")

bus1 = Bus()
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Charlie", 20)
person4 = Person("Diana", 22)
person5 = Person("Luis", 28)
person6 = Person("Eva", 27)
#invalid_person = Person("", -5)  # This should raise a ValueError
#invalid_person = Person("Pedrito", -5)  # This should raise a ValueError


bus1.board(person1)
#bus1.board("NotAPerson")  # This should raise a ValueError
bus1.board(person2)
bus1.board(person3)
bus1.board(person4)
bus1.board(person5)
bus1.board(person6)  # This should indicate the bus is full


print("==================")
bus1.unboard()
bus1.board(person6)  # Now Eva should be able to board
bus1.unboard()
print(f"Checking remaining capacity: {bus1.capacity} and occupied: {len(bus1.passengers)}")
bus1.unboard()
print(f"Checking remaining capacity: {bus1.capacity} and occupied: {len(bus1.passengers)}")
bus1.unboard()
print(f"Checking remaining capacity: {bus1.capacity} and occupied: {len(bus1.passengers)}")
bus1.unboard()
print(f"Checking remaining capacity: {bus1.capacity} and occupied: {len(bus1.passengers)}")
bus1.unboard()
print(f"Checking remaining capacity: {bus1.capacity} and occupied: {len(bus1.passengers)}")
bus1.unboard()  # This should indicate no passengers to unboard
print(f"Checking remaining capacity: {bus1.capacity} and occupied: {len(bus1.passengers)}")
bus1.unboard()
print(f"Checking remaining capacity: {bus1.capacity} and occupied: {len(bus1.passengers)}")
