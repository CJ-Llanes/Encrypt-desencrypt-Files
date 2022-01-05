from cryptography.fernet import Fernet

def desencript(encripted, privateKey):
    with open(privateKey, 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open(encripted, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    #with open("tmp_"+encripted, 'wb') as dec_file:
        #dec_file.write(decrypted)
    return decrypted