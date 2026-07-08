class PartyAnimal:
    # Constructor: similar to a Java constructor
    # It runs when we create a new object of this class.
    def __init__(self, name, secondName):
        # Store the name passed as an argument in the object.
        self.name = name
        self.secondName = secondName
        # Initialize the counter to 0.
        self.x = 0

    # Method: similar to a Java method
    # It increases the counter and prints the result.
    def party(self):
        # Increase the counter by 1.
        self.x = self.x + 1
        # Print the name and the current count.
        print(self.name,"-", self.secondName, "party count", self.x)


# Create an object of the class (similar to 'new PartyAnimal("Sally")' in Java)
animal = PartyAnimal("Sally", "Smith")
# Call the method several times
animal.party()
animal.party()
animal.party()