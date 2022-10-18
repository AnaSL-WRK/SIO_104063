import secrets
from cryptography.fernet import Fernet
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


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

    fileInput = open(nameIn, 'rb')
    FileIn = fileInput.read()


    try:
        fileOut = open(nameOut, 'xb')
    except FileExistsError:
        fileOut = open(nameOut, 'wb')

    


    
    nonce = os.urandom(16) #does chacha need this or is it the same as iv
    iv = secrets.token_bytes(16)
    fileOut.write(iv)                       #passing iv as first 16 bytes of the file for later decryption
    fileOut.close          
   
                                                        #Should be unique, a nonce. It is critical to never 
                                                        #reuse a nonce with a given key. Any reuse of a nonce with the same 
                                                        #key compromises the security of every message encrypted with that key.
                                                        #The nonce does not need to be kept secret and may be included with the ciphertext. 
                                                        #This must be 128 bits in length. The 128-bit value is a concatenation of 4-byte
                                                        #little-endian counter and the 12-byte nonce 
    if alg == "chacha20":
            algorithm = algorithms.ChaCha20(key, iv)
            cipher = Cipher(algorithm, mode=None)
    elif alg == "aes":
            algorithm = algorithms.AES(key)
            if  mode == "cfb":
                cipher = Cipher(algorithms.AES(key),modes.CFB(iv))
            elif mode == "obf":
                cipher = Cipher(algorithms.AES(key),modes.OFB(iv))
            elif mode == "ecb":
                cipher = Cipher(algorithms.AES(key),modes.ECB())
            elif mode == "cbc":
                cipher = Cipher(algorithms.AES(key),modes.CBC(iv))


                                         
    encryptor = cipher.encryptor()    


    padder = padding.PKCS7(128).padder() 
   
    ct = encryptor.update(FileIn) #+ encryptor.finalize()
    padded_data = padder.update(ct)                                      
    ct = encryptor.update(padded_data)
                                          
    ivExp = iv.decode('latin-1') 
    print("IV: " + ivExp + " appended to file")


    fileOut = open(nameOut, 'ab')
    fileOut.write(ct)              
    fileOut.close
    
  # decryptor = cipher.decryptor()
  # out = decryptor.update(ct)
  # print(out)



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
    else: 
        mode == None

    #testing
    #nameIn = "text.txt"
    #nameOut = "output.txt"
    #alg = "aes"
    #key = None
    #mode = "ecb"


    encrypt(nameIn, nameOut, alg, key, mode)
    
    
if __name__ == main():
    main()

