## This lecture introduces the concept of working with files in Python, marking a shift from temporary in-memory data to permanent storage.
    #Understanding File Interaction

    #Files provide a way to store data permanently, unlike variables that exist only during program execution.
    #The lecture uses flat text files, which are simple files consisting of lines of text, such as email mailbox files.
    #Opening and Handling Files in Python

    #To work with a file, Python must first open it, which creates a file handle—a connection to the file, not the file's content itself.
    #The open function is used with the filename and mode (read or write), returning a file handle to interact with the file.
    # File Structure and Newline Characters

    #Files are sequences of characters separated by newline characters, which represent the Enter key and move the cursor to the next line.
    #Newlines are a single non-printing character represented as "\n" in strings, crucial for understanding how text files are structured and read.
    #This sets the foundation for reading from and writing to files in Python, enabling programs to interact with real-world data stored on disk.


fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print("There were", count, "subject lines in", fname)


    