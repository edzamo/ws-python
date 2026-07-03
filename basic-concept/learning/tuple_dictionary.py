#The first and the clearest distinction between lists and tuples is the syntax used to create 
# them - tuples prefer to use parenthesis, whereas lists like to see brackets, although it's 
# also possible to create a tuple just from a set of values separated by commas.

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)



#1. Tuples are ordered and unchangeable (immutable) collections of data. 
# They can be thought of as immutable lists. They are written in round brackets:
my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(my_tuple)

my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(my_list)

#2. You can create an empty tuple like this:
empty_tuple = ()
print(type(empty_tuple))    # outputs: <class 'tuple'>

#3. A one-element tuple may be created as follows:
one_elem_tuple_1 = ("one", )    # Brackets and a comma.
one_elem_tuple_2 = "one",       # No brackets, just a comma.

#4. You can access tuple elements by indexing them:
my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
print(my_tuple[3])    # outputs: [3, 4]

#5. Tuples are immutable, which means you cannot change their elements (you cannot append tuples, or modify, 
# or remove tuple elements). The following snippet will cause an exception:
my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
my_tuple[2] = "guitar"    # The TypeError exception will be raised.

pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

print(len(pol_eng_dictionary))    # outputs: 3
del pol_eng_dictionary["zamek"]    # remove an item
print(len(pol_eng_dictionary))    # outputs: 2

pol_eng_dictionary.clear()   # removes all the items
print(len(pol_eng_dictionary))    # outputs: 0

del pol_eng_dictionary    # removes the dictionary

