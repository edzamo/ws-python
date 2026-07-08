name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = {}
for line in handle:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    parts = line.split()
    if len(parts) < 2:
        continue
    email = parts[1]
    counts[email] = counts.get(email, 0) + 1

handle.close()

print("Email counts:" , counts)

most_sender = None
most_count = 0
for sender, count in counts.items():
    if count > most_count:
        most_sender = sender
        most_count = count
        print("look", sender, count)

if most_sender is not None:
    print(most_sender, most_count)
else:
    print("No senders found")
