from cryptography.fernet import Fernet
import os

def encript(filename, privateKey):
    print(filename,os.getcwd(), privateKey)
    try:
        key=open(privateKey, "r").read()
        original=open(filename, "r").read()
    except IndexError:
        print("Error: a problem ocurred while loading the files")
    
    fernet=Fernet(key)
    encrypted = fernet.encrypt(original)
    return encrypted