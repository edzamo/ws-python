"""
Examples for web services, serialization, and JSON data exchange.
"""

import json


def example_json_serialization():
    data = {
        "name": "Edwin",
        "age": 25,
        "skills": ["Python", "Web Data"],
        "active": True,
    }

    print("Original Python data:")
    print(data)

    json_text = json.dumps(data)
    print("\nSerialized to JSON:")
    print(json_text)

    restored_data = json.loads(json_text)
    print("\nDeserialized back to Python:")
    print(restored_data)
    print("Type:", type(restored_data).__name__)


def example_json_from_web_like_payload():
    payload = '{"user": "Ana", "score": 90, "completed": true}'
    parsed = json.loads(payload)
    print("\nParsed payload:")
    print(parsed)
    print("User:", parsed["user"])


if __name__ == "__main__":
    example_json_serialization()
    example_json_from_web_like_payload()
