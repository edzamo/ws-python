"""
Examples for character encoding and Unicode in Python.
"""

# 1. ASCII example
print("ASCII example")
letter = 'A'
print("Character:", letter)
print("ASCII code:", ord(letter))
print("Character from code:", chr(65))
print()

# 2. Unicode example
print("Unicode example")
word = "Hola"
print("Unicode string:", word)
for ch in word:
    print(ch, "->", ord(ch))
print()

# 3. UTF-8 encoding and decoding
print("UTF-8 example")
text = "café"
encoded = text.encode("utf-8")
print("Original:", text)
print("Encoded bytes:", encoded)
print("Decoded back:", encoded.decode("utf-8"))
print()

# 4. Example of bytes sent over a socket-like communication
print("Bytes example")
message = "Python ❤️ Unicode"
encoded_message = message.encode("utf-8")
print("Encoded bytes:", encoded_message)
print("Decoded string:", encoded_message.decode("utf-8"))
print()

# 5. ASCII compatibility check
print("ASCII compatibility")
print("'hello' in ASCII:", 'hello'.isascii())
print("'café' in ASCII:", 'café'.isascii())
