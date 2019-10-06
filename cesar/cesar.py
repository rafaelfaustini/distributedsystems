import sys
import string

def encrypt(text,rotation):
    alphabet = string.ascii_lowercase
    result = ''
    for letter in text:
        if letter in alphabet:
            p = alphabet.find(letter)
            p = (p+rotation)%26
            result += alphabet[p]
    return result

def decrypt(text, rotation):
    alphabet = string.ascii_lowercase
    result = ''
    for letter in text:
        if letter in alphabet:
            p= alphabet.find(letter)
            p= (p-rotation)%26
            result += alphabet[p]
    return result

