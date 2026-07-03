numbers = [10, 5, 7, 2, 1]
print("1 Original list contents:", numbers)  # Printing original list contents.

numbers[0] = 111
print("\n 2 Previous list contents:", numbers)  # Printing previous list contents.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("3 New list contents:", numbers)  # Printing current list contents.

numbers = [10, 5, 7, 2, 1]
print("4 Original list contents:", numbers)  # Printing original list contents.

numbers[0] = 111
print("\nPrevious list contents:", numbers)  # Printing previous list contents.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("6 Previous list contents:", numbers)  # Printing previous list contents.

print("\n 7List length:", len(numbers))  # Printing the list's length.

print("\n Removing elements from a list")

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.


numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#
print("###############")

my_list = [10, 1, 8, 3, 5]
total = 0
 
for i in my_list:
    print(i)
    total += i
 
print(total)
 

lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)

