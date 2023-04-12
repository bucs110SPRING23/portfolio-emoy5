def decipher(text, shift):
    """
    Encrypts or decrypts a message using the Caesar cipher technique.

    args:
        text:str = the message to encrypt or decrypt
        shift:int = the number of positions to shift each letter
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
    
    fptr = open("encrypted-#B00874795.txt", "r")
    encryptedtxt = fptr.read()
    fptr_decrypt = open("decrypted.txt", "w")
    fptr_decrypt.write(str(decipher(encryptedtxt,13)))
    fptr.close()
    fptr_decrypt.close()

main()