import secrets
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding



def makeKey(key, alg=None):
 
    if key is None:   
       key = Fernet.generate_key()
    else:
        key = bytes(key,'utf-8')
       
   
    if alg == "chacha20":
        key = key[:32]
    elif alg == "aes":
        key = key[:16]

    try:
        file = open('key.key', 'xb')
    except FileExistsError:
        file = open('key.key', 'wb')

    file.write(key)                 #type bytes
    file.close()

    
   
   
   
   
def encrypt(nameIn,nameOut,alg,key,mode):
    
    
    alg = alg.lower()
    




    try:
        encModes = open("algorithm.txt", 'x')
    except FileExistsError:
        encModes = open("algorithm.txt", 'w')


    if alg == "aes":
        if mode == None:
            mode == "cfb"
        else: 
            mode = mode.lower()
        encModes.write(alg + "\n" + mode)
    else:
         encModes.write(alg)






    makeKey(key,alg)
    file = open('key.key', 'rb')

    key = file.read()
    file.close()

    fileInput = open(nameIn, 'rb')
    msg = fileInput.read()


    try:
        fileOut = open(nameOut, 'xb')
    except FileExistsError:
        fileOut = open(nameOut, 'wb')

    

    iv = secrets.token_bytes(16)
   # fileOut.write(iv)                       #passing iv as first 16 bytes of the file for later decryption
   # fileOut.close()       


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
            else:
                 print ("Invalid mode, please try another one")
                 exit
    else:
        print ("Invalid algorithm, please try another one")
        exit







    encryptor = cipher.encryptor()    

    padder = padding.PKCS7(128).padder() 
   
    padded_data = padder.update(msg) + padder.finalize()                                 
    ct = encryptor.update(padded_data) + encryptor.finalize()


    ivExp = iv.decode('latin-1') 
    print("IV: " + ivExp + " appended to file")


    fileOut = open(nameOut, 'ab+')
    fileOut.write(ct)
        


def main():   

  #nameIn, nameOut, alg = input("Write what file to encrypt, where you want the output and the algorythm to use (chacha20 or aes) \n").split()
  #
  #ans = input("do you have a key? [Y/N] ")
  #ans = ans.lower()

  #if ans == "y":
  #    key = input("paste your key here \n")
  #else:
  #    key = None

  #if alg == "aes":
  #    mode = input("What mode do you want? (CFB(default), OBF, ECB, CBC) \n" )
  #    if mode == None:
  #        mode == None
  #else: 
  #    mode == None

    #testing
    nameIn = "text.txt"
    nameOut = "encoded.txt"
    alg = "aes"
    key = None
    mode = "ecb"

    #o git ta maluco

    encrypt(nameIn, nameOut, alg, key, mode)
    
    
if __name__ == main():
    main()

