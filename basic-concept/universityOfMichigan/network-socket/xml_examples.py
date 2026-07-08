"""
Examples for XML structure, parsing, and data exchange in Python.
"""

import xml.etree.ElementTree as ET


def create_xml_example():
    person = ET.Element("person")
    person.set("id", "1")

    name = ET.SubElement(person, "name")
    name.text = "Edwin"

    email = ET.SubElement(person, "email")
    email.text = "edwin@example.com"

    print("Created XML:")
    print(ET.tostring(person, encoding="unicode"))


def parse_xml_example():
    xml_data = """
    <people>
        <person id="2">
            <name>Ana</name>
            <email>ana@example.com</email>
        </person>
        <person id="3">
            <name>Luis</name>
            <email>luis@example.com</email>
        </person>
    </people>
    """

    root = ET.fromstring(xml_data)
    print("\nParsed XML root:", root.tag)

    for person in root.findall("person"):
        print("Person id:", person.get("id"))
        print("Name:", person.findtext("name"))
        print("Email:", person.findtext("email"))


if __name__ == "__main__":
    create_xml_example()
    parse_xml_example()
