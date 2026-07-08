def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)

hi_all("Sebastian", "Konrad")


def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)

s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")
address(s, c, p_c)



def list_sum(lst):
    s = 0
 
    for elem in lst:
        s += elem
 
    return s


print("Sum of the list:", list_sum([1, 2, 3, 4, 5]))
