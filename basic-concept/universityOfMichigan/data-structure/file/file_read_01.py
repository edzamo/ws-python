from pathlib import Path

file_path = Path("file_python.txt")

file_handler=open(file_path, 'r')
x=0
for line in file_handler:
    x=x+1
print("There were", x, "lines in the file.")

file_handler.close()   