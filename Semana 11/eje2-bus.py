class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class bus:
    def __init__(self):
        self.capacity = 5
        self.passengers = []
    
    def board(self, person):
        if self.capacity > 0:
            self.capacity -= 1
            print(f"{person.name} boarded the bus with age {person.age}. Remaining capacity: {self.capacity}")
            self.passengers.append(person)
        else:
            print("Bus is full. Cannot board more passengers.")
    
    def unboard(self):
        self.capacity += 1
        if len(self.passengers) > 0:
            person = self.passengers.pop(0)
            print(f"{person.name} unboarded the bus with age {person.age}. Remaining capacity: {self.capacity}")
        else:
            print("No passengers to unboard.")

bus1 = bus()
person1 = person("Alice", 30)
person2 = person("Bob", 25)
person3 = person("Charlie", 20)
person4 = person("Diana", 22)
person5 = person("Luis", 28)
person6 = person("Eva", 27)

bus1.board(person1)
bus1.board(person2)
bus1.board(person3)
bus1.board(person4)
bus1.board(person5)
bus1.board(person6)  # This should indicate the bus is full

bus1.unboard()
bus1.board(person6)  # Now Eva should be able to board
bus1.unboard()
bus1.unboard()
bus1.unboard()
bus1.unboard()
bus1.unboard()
bus1.unboard()  # This should indicate no passengers to unboard




