"""
Inheritance examples for OOP.
This file shows how a child class can reuse and extend a parent class.
"""


class PartyAnimal:
    # Parent class (base class)
    # It defines common behavior that other classes can reuse.
    def __init__(self, name):
        # Each object gets its own name.
        self.name = name
        # Each object has its own counter.
        self.x = 0
        print(self.name, "was created")

    # Common method for all PartyAnimal objects.
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)


class FootballFan(PartyAnimal):
    # Child class (derived class)
    # It inherits from PartyAnimal and adds new behavior.
    def __init__(self, name):
        # Call the parent constructor to initialize the name and counter.
        super().__init__(name)
        # Add a new attribute only for FootballFan.
        self.points = 0
        print(self.name, "is now a football fan")

    # New method added only to the child class.
    def touchdown(self):
        self.points = self.points + 6
        print(self.name, "scored a touchdown! Total points:", self.points)


class Student(PartyAnimal):
    # Another child class that extends the base class.
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def show_grade(self):
        print(self.name, "has grade", self.grade)


if __name__ == "__main__":
    # Create a parent object.
    animal = PartyAnimal("Sally")
    animal.party()

    # Create a child object that inherits parent behavior.
    fan = FootballFan("Tom")
    fan.party()      # inherited from PartyAnimal
    fan.touchdown()  # new method in FootballFan

    # Create another child object.
    student = Student("Ana", 90)
    student.party()      # inherited from PartyAnimal
    student.show_grade() # new method in Student
