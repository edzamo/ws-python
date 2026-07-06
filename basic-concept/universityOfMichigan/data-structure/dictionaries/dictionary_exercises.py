"""
Dictionary practice exercises for the `universityOfMichigan/data-structure/dictionaries` project.

Each exercise shows a common dictionary use case and includes a simple solution.
"""

# Exercise 1: Word frequency histogram
# Read a line of text, count each word, and print the counts.

def word_frequency():
    text = input("Enter a line of text: ")
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    print("Word counts:")
    for word, count in counts.items():
        print(word, count)


# Exercise 2: Email domain counter
# Read email addresses until the user types 'done', then count email domains.

def email_domain_counter():
    counts = {}
    while True:
        email = input("Enter email address (or done): ")
        if email == "done":
            break
        if "@" not in email:
            print("Invalid email format, try again.")
            continue
        domain = email.split("@")[1]
        counts[domain] = counts.get(domain, 0) + 1

    print("Domain counts:")
    for domain, count in counts.items():
        print(domain, count)


# Exercise 3: Simple phonebook lookup
# Store names and phone numbers in a dictionary, then look up a requested name.

def phonebook_lookup():
    phonebook = {
        "Ana": "555-1234",
        "Luis": "555-5678",
        "Sara": "555-9012"
    }

    name = input("Enter a name to look up: ")
    number = phonebook.get(name)
    if number is None:
        print("Not found")
    else:
        print(name, "->", number)


# Exercise 4: Average score by student
# Read student score lines and compute the average for each student.

def student_score_average():
    totals = {}
    counts = {}
    while True:
        line = input("Enter name and score (or done): ")
        if line == "done":
            break
        parts = line.split()
        if len(parts) != 2:
            print("Please enter a name and a score.")
            continue
        name, score_str = parts
        try:
            score = float(score_str)
        except ValueError:
            print("Score must be a number.")
            continue

        totals[name] = totals.get(name, 0.0) + score
        counts[name] = counts.get(name, 0) + 1

    print("Average scores:")
    for name in totals:
        average = totals[name] / counts[name]
        print(name, average)


if __name__ == "__main__":
    print("Dictionary exercise module")
    print("Use the functions: word_frequency(), email_domain_counter(), phonebook_lookup(), or student_score_average().")
