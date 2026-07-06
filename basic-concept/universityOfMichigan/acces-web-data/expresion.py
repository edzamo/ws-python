"""
Regular expression examples for the `acces-web-data` class.
Run this module directly to see example outputs.
"""
import re


def example_search():
    text = "Contact: alice@example.com and bob@domain.org"
    m = re.search(r"[\w.-]+@[\w.-]+", text)
    print("search ->", m.group() if m else "no match")


def example_findall():
    text = "Prices: $5.00, $12.50, and $100"
    prices = re.findall(r"\$\d+(?:\.\d{2})?", text)
    print("findall ->", prices)


def example_groups():
    text = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
    m = re.search(r"From\s+(\S+@\S+)\s+.*(\d{2}:\d{2}:\d{2})", text)
    if m:
        print("groups -> email:", m.group(1), "time:", m.group(2))
    else:
        print("groups -> no match")


def example_sub():
    text = "<b>bold</b> and <i>italic</i>"
    cleaned = re.sub(r"<.*?>", "", text)
    print("sub ->", cleaned)


def example_compile():
    pattern = re.compile(r"https?://[\w./-]+")
    text = "Visit https://example.com or http://test.org/page"
    print("compile findall ->", pattern.findall(text))


if __name__ == "__main__":
    print("Regular expression examples:\n")
    example_search()
    example_findall()
    example_groups()
    example_sub()
    example_compile()
