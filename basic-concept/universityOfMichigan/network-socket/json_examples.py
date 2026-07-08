"""
Examples for JSON data structures and parsing in Python.
"""

import json


def create_json_example():
    data = {
        "name": "Edwin",
        "age": 25,
        "skills": ["Python", "Web Data"],
        "address": {
            "city": "Guayaquil",
            "country": "Ecuador"
        }
    }

    json_text = json.dumps(data, indent=2)
    print("JSON text:")
    print(json_text)


def parse_json_example():
    json_text = '{"name": "Ana", "scores": [90, 85, 92], "active": true}'
    parsed = json.loads(json_text)

    print("\nParsed JSON:")
    print(parsed)
    print("Name:", parsed["name"])
    print("First score:", parsed["scores"][0])


def iterate_json_array():
    json_text = '[{"name": "Luis"}, {"name": "Sara"}, {"name": "Mina"}]'
    people = json.loads(json_text)

    print("\nPeople:")
    for person in people:
        print(person["name"])


if __name__ == "__main__":
    create_json_example()
    parse_json_example()
    iterate_json_array()
