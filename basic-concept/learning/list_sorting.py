#Sorting a list
my_list = [8, 10, 6, 2, 4]  # list to sort
print("Original list:", my_list)


for i in range(len(my_list) - 1):  # we need (5 - 1) comparisons
    if my_list[i] > my_list[i + 1]:  # compare adjacent elements
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # If we end up here, we have to swap the elements.

print("Sorted list:", my_list)


print("#################")

my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.
cont = 0  # counter for swaps
while swapped:
    swapped = False  # no swaps so far
    cont = 0 
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            cont+=1
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] #in java need to use a temp variable
    
    print("Number of swaps in this iteration:", cont)

print("Sorted list:", my_list)