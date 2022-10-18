
from msilib.schema import File
import secrets
from cryptography.fernet import Fernet
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from PIL import Image
from PIL import BmpImagePlugin
from cryptography.hazmat.primitives import padding
import numpy as np
from cryptography.hazmat.backends import default_backend

def makeKey(key, alg=None):
 
    if key is None:   
       key = Fernet.generate_key()
    else:
        key = bytes(key,'utf-8')

    ## diff algs need diff key lengths
    if alg == "chacha20":
        key = key[:32]
    elif alg == "aes":
        key = key[:16]

    try:
        file = open('key.key', 'xb')
    except FileExistsError:
        file = open('key.key', 'wb')

    file.write(key)                 #type bytes
    file.close

    
   
   
   
   
def encrypt(nameIn,nameOut,alg,key,mode):
    
    alg = alg.lower()

    if mode == None:
        mode == "cfb"

    mode = mode.lower()
    
    makeKey(key,alg)
    file = open('key.key', 'rb')

    key = file.read()
    file.close


    try:
        img=Image.open(nameIn)
        Imgsave = img.save("frangos.bmp")
        #temp = img.convert(mode ="1")
        #FileIn = temp.tobitmap()
        FileIn = img.tobytes("hex","rgb")
        

    except IOError:
        file = open(nameIn, 'rb')          
        FileIn = file.read()
    
    
    nonce = os.urandom(16)
    iv = secrets.token_bytes(16)
   
                                                        #Should be unique, a nonce. It is critical to never 
                                                        #reuse a nonce with a given key. Any reuse of a nonce with the same 
                                                        #key compromises the security of every message encrypted with that key.
                                                        #The nonce does not need to be kept secret and may be included with the ciphertext. 
                                                        #This must be 128 bits in length. The 128-bit value is a concatenation of 4-byte
                                                        #little-endian counter and the 12-byte nonce 
                                                        #little-endian counter and the 12-byte nonce 
    if alg == "chacha20":
            algorithm = algorithms.ChaCha20(key, nonce)
            cipher = Cipher(algorithm, mode=None)
    elif alg == "aes":
            if  mode == "cfb":
                cipher = Cipher(algorithms.AES(key),modes.CFB(iv), default_backend())
            elif mode == "obf":
                cipher = Cipher(algorithms.AES(key),modes.OFB(iv))
            elif mode == "ecb":
                cipher = Cipher(algorithms.AES(key),modes.ECB())
            elif mode == "cbc":
                cipher = Cipher(algorithms.AES(key),modes.CBC(iv))


                                         
    encryptor = cipher.encryptor()    


    padder = padding.PKCS7(128).padder() 
   
    ct = encryptor.update(FileIn) 
    padded_data = padder.update(ct)                                      
    ct = encryptor.update(padded_data)

 

    output_image = img.copy()
    output_image.frombytes(ct)
    output_image.save(nameOut)




def main():   

    nameIn, nameOut, alg = input("Write what file to encrypt, where you want the output and the algorythm to use (chacha20 or aes) \n").split()
    
    ans = input("do you have a key? [Y/N] ")
    ans = ans.lower()

    if ans == "y":
        key = input("paste your key here \n")
    else:
        key = None

    if alg == "aes":
        mode = input("What mode do you want? (CFB(default), OBF, ECB, CBC) \n" )
        if mode == None:
            mode == None


    #testing
    #nameIn = "Totoro.jpg"
    #nameOut = "ecb.bmp"
    #alg = "aes"
    #key = None
    #mode = "ecb"




    encrypt(nameIn, nameOut, alg, key, mode)

    print("Done")


if __name__ == main():
    main()