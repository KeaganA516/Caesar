secret_messge = "Somewhere over the rainbow 123+."
number = 3

def caesar_cipher(text: str, shift: int):
    result = ""

    for char in text:
        if char .islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char .isdigit():
            result += chr((ord(char) + shift - 48) % 10 + 48)
        else:
           result += char
          
    return result

def caesar_cipher(secret_message : str, shift: int):
    result = ""

    for char in secret_messge:
        if char .islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char .isdigit():
            result += chr((ord(char) - shift - 48) % 10 + 48)
        else:
           result += char

print(caesar_cipher(secret_messge, number))

