import random

def cipher(text):
    """
    Encrypts or decrypts a message.

    args:
        text:str = the message to encrypt or decrypt
    return:
        :str = the encrypted or decrypted message
    """
    
    text_list = []
    for char in text:
        text_list.append(char)
    
    result = ""    
    for pos, ltr in enumerate(text_list):
        if ltr == " ":
            result += ltr
        elif ltr.isalpha():
            start = ord('A') if ltr.isupper() else ord('a')
            if text_list[pos-1] == "" or " ":
                new_pos = (ord(text_list[pos]) - start + 8) % 26
            elif ltr.isalpha():
                new_pos = (ord(text_list[pos-1]) - start + 4) % 26
            ltr = chr(start + new_pos)
        result += ltr
    return result

def main():
    
    fptr = open("encrypted.txt", 'w')
    fptr.write(str(cipher("The quick brown fox jumps over the lazy dog")))
    fptr.close()

main()