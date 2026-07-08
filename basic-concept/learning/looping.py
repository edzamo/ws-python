# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

# Looping with a for loop


for i in range(10):
    print("The value of i is currently", i)


for i in range(2, 8):
    print("The value of i is currently", i)

#The third argument is an increment – it's a value added to control 
# the variable at every loop turn (as you may suspect, the default value of the increment is 1).
for i in range(2, 9, 2):
    print("The value of i is currently", i)

