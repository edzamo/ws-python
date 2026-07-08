from pathlib import Path

file_path = Path("mbox-short.txt")
file_handler=open(file_path, 'r')
words=[]
domains = []
for line in file_handler:
    line = line.rstrip()
    if not line.startswith("From:"):
        continue
    words.append(line.split()[1])
  

for word in words:
    domain = word.split('@')[1]
    if domain not in domains:
        domains.append(domain)


print('the number of unique email addresses is:', len(domains))
print('the number of unique email addresses is:', domains)
print('the number of lines in the file is:', len(words))



file_handler.close()   

x = list(range(5))
print(x)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b #in python, the + operator concatenates lists
print(len(c))