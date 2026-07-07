"""
Additional OOP exercises for the Python class topic.
These examples help practice classes, methods, instance attributes, and object inspection.
"""


class Dog:
    """A simple class representing a dog."""

    def __init__(self, name):
        self.name = name
        self.energy = 0

    def bark(self):
        print(self.name, "says woof!")

    def play(self):
        self.energy += 1
        print(self.name, "is playing. Energy:", self.energy)


class Student:
    """A class to store student information."""

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passing(self):
        return self.grade >= 70

    def show_info(self):
        print(self.name, "has grade", self.grade)


class Counter:
    """A simple counter class."""

    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0


if __name__ == "__main__":
    print("Dog example")
    dog = Dog("Max")
    dog.bark()
    dog.play()

    print("\nStudent example")
    student = Student("Ana", 85)
    student.show_info()
    print("Passing?", student.is_passing())

    print("\nCounter example")
    counter = Counter()
    counter.increment()
    counter.increment()
    print("Counter value:", counter.value)
    counter.reset()
    print("Reset value:", counter.value)
