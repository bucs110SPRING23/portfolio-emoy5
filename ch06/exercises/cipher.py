import random

def cipher(text):
    """
    Encrypts or decrypts a message.

    args:
        text:str = the message to encrypt or decrypt
    return:
        :str = the encrypted or decrypted message
    """

    result = ""
    for char in text:
        if char.isalpha():
            # Determine the case of the character
            start = ord('A') if char.isupper() else ord('a')
            # Calculate the new position of the character after the shift
            new_pos = (ord(char) - start + shift) % 26
            # Convert the new position back to a character
            char = chr(start + new_pos)
        result += char
    return result

def main():
    
    fptr = open("encrypted.txt", 'w')
    fptr.write(str(cipher("The quick brown fox jumps over the lazy dog")))
    fptr.close()

main()