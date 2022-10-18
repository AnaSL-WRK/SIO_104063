from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from msilib.schema import File
from tokenize import String
from cryptography.fernet import Fernet

import sys
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
key = os.urandom(32)
nonce = os.urandom(16)

algorithm = algorithms.ChaCha20(key, nonce)
cipher = Cipher(algorithm, mode=None)
encryptor = cipher.encryptor()

file = open( "text.txt", 'br')
FileIn = file.read()

print(FileIn) 
ct = encryptor.update(FileIn)


decryptor = cipher.decryptor()
iu = decryptor.update(ct)
print(iu)