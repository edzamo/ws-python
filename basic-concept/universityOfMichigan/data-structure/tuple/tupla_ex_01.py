name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"

try:
    handle = open(name)
except FileNotFoundError:
    print(f"File not found: {name}")
    raise

# Build a dictionary that maps hour -> count
counts = {}
for line in handle:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    parts = line.split()
    # Find the token that looks like a time (contains ':'), e.g. '09:14:16'
    time_token = None
    for token in parts:
        if ':' in token:
            time_token = token
            break
    if time_token is None:
        continue
    hour = time_token.split(':')[0]
    counts[hour] = counts.get(hour, 0) + 1

handle.close()

# Print the counts sorted by hour
for hour in sorted(counts.keys()):
    print(hour, counts[hour])