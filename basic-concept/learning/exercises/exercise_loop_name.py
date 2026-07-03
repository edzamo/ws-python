# Prompt the user to enter a word
# and assign it to the user_word variable.

letter= input("Please enter a word: ")
for i in range(len(letter)):
    # Complete the body of the for loop.
    vowel = "aeiou"
    if letter[i].lower() not in vowel:
        print("The current letter is:",  letter[i].upper())
    


#
#3.3.7 SECTION SUMMARY
#1. Python supports the following logical operators:

#and → if both operands are true, the condition is true, e.g., (True and True) is True,
#or → if any of the operands are true, the condition is true, e.g., (True or False) is True,
#not → returns false if the result is true, and returns true if the result is false, e.g., not True is False.
#2. You can use bitwise operators to manipulate single bits of data. The following sample data:

#x = 15, which is 0000 1111 in binary,
#y = 16, which is 0001 0000 in binary.
#will be used to illustrate the meaning of bitwise operators in Python. Analyze the examples below:

#& does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary,
#| does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary,
#˜  does a bitwise not, e.g., ˜ x = 240*, which is 1111 0000 in binary,
#^ does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary,
#>> does a bitwise right shift, e.g., y >> 1 = 8, which is 0000 1000 in binary,
#<< does a bitwise left shift, e.g., y << 3 = 128, which is 1000 0000 in binary.
#* -16 (decimal from signed 2's complement) -- read more about the Two's complement operation.