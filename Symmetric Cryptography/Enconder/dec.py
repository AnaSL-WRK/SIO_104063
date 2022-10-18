
###not done

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from msilib.schema import File
from tokenize import String
from cryptography.fernet import Fernet

import sys
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

nonce = os.urandom(16)

file = open( "key.key", 'br')
key = file.read()


file = open( "output.txt", 'br')
FileIn = file.read()

algorithm = algorithms.ChaCha20(key, nonce)
cipher = Cipher(algorithm, mode=None)


decryptor = cipher.decryptor()
out = decryptor.update(FileIn)
print(out)
