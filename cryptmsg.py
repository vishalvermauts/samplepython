#!/usr/bin/env python3
import time
import sys

def caesar_cipher_decrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

def type_with_sound(message, delay=0.1):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        print('\a', end='', flush=True) 
        time.sleep(delay)
if __name__ == "__main__":
    encrypted_message = (
        "Xlmw mw e wigvix qiwweki."
        "Srpc xli asvxlc ger higmtliv mx."
        "Aipgsqi xs xli qcwxivmsyw asvph sj Tcxlsr!"
        "Oiit xlmw gshi weji erh wigyvi."
       "Xli xvyxl mw syx xlivi."
    ) 
    shift = 4
    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
    type_with_sound(decrypted_message)
#This is Not a Drill