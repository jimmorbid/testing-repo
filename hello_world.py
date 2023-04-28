def hello_world():
    print("Hello, World!")

def rot13(text):
    """
    Convert text to ROT13 ciphered text.
    """
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - 97 + 13) % 26 + 97)
            else:
                result += chr((ord(char) - 65 + 13) % 26 + 65)
        else:
            result += char
    return result

# Ask the user to enter some text
text = input("Enter some text: ")

# Convert the text to ROT13 ciphered text
rot13_text = rot13(text)

# Print the ROT13 ciphered text
print("ROT13 ciphered text: " + rot13_text)
