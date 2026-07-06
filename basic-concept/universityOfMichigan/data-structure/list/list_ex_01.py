file_name = input("Enter the file name: ")
file_handler = open(file_name)

lst = list()
for line in file_handler:
    words = line.rstrip().split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)



