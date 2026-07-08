"""
Tuple practice exercises for the `universityOfMichigan/data-structure/tuple` project.

This module contains several simple examples and exercises to help understand tuples.
"""

# Exercise 1: Create and print a tuple
# Create a tuple of your five favorite fruits and print it.

def exercise_create_tuple():
    fruits = ("apple", "banana", "cherry", "date", "elderberry")
    print("Tuple:", fruits)
    print("First fruit:", fruits[0])
    print("Last fruit:", fruits[-1])


# Exercise 2: Count and find
# Count how many times a value appears and find its index.

def exercise_count_find():
    numbers = (1, 2, 2, 3, 4, 2, 5)
    count_2 = numbers.count(2)
    first_2 = numbers.index(2)
    print("Tuple:", numbers)
    print("Count of 2:", count_2)
    print("First index of 2:", first_2)


# Exercise 3: Tuple immutability
# Try to modify a tuple and show how to create a new one instead.

def exercise_immutable():
    original = ("red", "green", "blue")
    print("Original tuple:", original)
    try:
        original[1] = "yellow"
    except TypeError as e:
        print("Error:", e)

    # Create a new tuple with one changed value
    modified = original[:1] + ("yellow",) + original[2:]
    print("Modified tuple:", modified)


# Exercise 4: Tuple unpacking
# Unpack a tuple into variables and use the values.

def exercise_unpacking():
    person = ("Alice", 30, "Engineer")
    name, age, profession = person
    print("Name:", name)
    print("Age:", age)
    print("Profession:", profession)


if __name__ == "__main__":
    print("Tuple exercises module")
    print("Run the functions: exercise_create_tuple(), exercise_count_find(), exercise_immutable(), exercise_unpacking().")
    exercise_count_find()
    
