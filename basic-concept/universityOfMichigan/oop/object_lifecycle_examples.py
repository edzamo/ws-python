"""
Object lifecycle examples for OOP.
This file shows how objects are created, how each object keeps its own data,
and how cleanup can be handled.
"""


class PartyAnimal:
    # Constructor-like method: runs when we create a new object.
    # In Java, this is similar to a constructor.
    def __init__(self, name):
        # Each object gets its own name.
        self.name = name
        # Each object has its own counter.
        self.x = 0
        print(self.name, "was created")

    # Method: changes the object's state.
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

    # Destructor-like method: runs when the object is about to be removed.
    # In Python, this is not called immediately like in Java, but it is useful for cleanup.
    def __del__(self):
        print(self.name, "was destroyed")


class Student:
    # Another example with multiple objects and separate state.
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        print("Student", self.name, "created")

    def show_info(self):
        print(self.name, "has grade", self.grade)


if __name__ == "__main__":
    # Create first object.
    animal1 = PartyAnimal("Sally")
    animal1.party()

    # Create second object.
    animal2 = PartyAnimal("Tom")
    animal2.party()

    # Each object has its own separate counter.
    print("Sally's counter:", animal1.x)
    print("Tom's counter:", animal2.x)

    # Reassign the variable to show object replacement.
    animal1 = animal2
    print("Now animal1 points to the same object as animal2")

    # Create a Student object.
    student = Student("Ana", 90)
    student.show_info()
