
import io
import secrets
from cryptography.fernet import Fernet
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from PIL import Image
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
    file.close



    
def exportAlgorithm(alg,mode):

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
   

###############this conversion is bad!
def bmpData(nameIn):

    try:
        file=Image.open(nameIn)
        file.save("ImageIn.bmp")

        file = open(nameIn, "rb")
        FileIn = file.read()

    
    except IOError:
        file = open(nameIn, 'rb')          
        FileIn = file.read()

    file.close()
    return FileIn


def encrypt(nameIn,nameOut,alg,key,mode):
    
    
    exportAlgorithm(alg,mode)

    makeKey(key,alg)
    file = open('key.key', 'rb')
    key = file.read()
    file.close


    DataIn = bmpData(nameIn)


    nonce = os.urandom(16)
    iv = secrets.token_bytes(16)


    if alg == "chacha20":
            algorithm = algorithms.ChaCha20(key, nonce)
            cipher = Cipher(algorithm, mode=None)
    elif alg == "aes":
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
   
    padded_data = padder.update(DataIn) + padder.finalize()                                 
    ct = encryptor.update(padded_data) + encryptor.finalize()

    #image = Image.open(nameIn)
    #output_image = Image.new(image.mode, image.size)

   #output_image.save(nameOut)
    #stream = io.BytesIO(ct)
    #image = Image.open(stream)
    #image.show()
    output = open(nameOut, "wb")
    output.write(ct)
    

    

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


    #testing
    nameIn = "tux.bmp"
    nameOut = "ecbTux.bmp"
    alg = "aes"
    key = None
    mode = "ecb"




    encrypt(nameIn, nameOut, alg, key, mode)

    print("Done")


if __name__ == main():
    main()