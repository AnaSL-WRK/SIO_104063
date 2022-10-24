
###not done

import os
import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from msilib.schema import File
from tokenize import String
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding



def decrypt(nameIn,nameOut,key,iv,encMode):

    file = open( "key.key", 'br')
    key = file.read()

    if iv != None:
        ivRead = open(nameIn, "br") # opening for [r]eading as [b]inary
        iv = ivRead.read(16) # if you only wanted to read 512 bytes, do .read(512)

    file = open(encMode, "r")
    file = file.read()
    alg = file.split('\n', 1)[0]
    mode = file.split('\n', 1)[1]

   # with open(nameIn, 'rb') as file1:
   #     with open(nameIn, 'wb') as file2:
   #         file2.write(file1.read()[16:])
   #         file.close()


    encFile = open(nameIn, "rb+")
    encodedTxt = encFile.read()

    #data = file[16:]
    #encOut.seek(16,0) #<-- AttributeError: 'bytes' object has no attribute 'seek'
    #print(encOut.tell())
    #print(encOut)          

    #print(os.path.getsize(nameIn))


    if alg == "chacha20":
            algorithm = algorithms.ChaCha20(key, iv)
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
            else:
                 print ("Invalid mode, please append the correct one")
                 exit
    else:
        print ("Invalid algorithm, please append the correct one")
        exit

    decryptor = cipher.decryptor()


    unpadder = padding.PKCS7(128).unpadder()

    
    dec = decryptor.update(encodedTxt) + decryptor.finalize()

    unpadded_data = unpadder.update(dec) + unpadder.finalize()



    fileOut = open(nameOut, 'wb+')
    fileOut.write(unpadded_data)  
    fileOut.close



def main():   

    nameIn, nameOut, key = input("Write what file to decrypt, where you want the output and the key to decrypt \n").split()
    
    ans = input("do you have the Iv? [Y/N] ")
    ans = ans.lower()
#
    if ans == "y":
        iv = input("Paste the Iv string here  \n")
    else:
        iv = None
#
    ans = input("Do you have the encryption mode? [Y/N] ")
    ans = ans.lower()
#
    if ans == "y":
        encMode = input("In what file do you have that information ")
    else: 
        print("You need to know the encoding algorithm and mode in order to decode")
#



    #testing
    #nameIn = "encoded.txt"
    #nameOut = "decrypted.txt"
    #key = "key.key"
    #iv = "y"
    #encMode = "algorithm.txt"

    decrypt(nameIn, nameOut, key, iv, encMode)
    
    
if __name__ == main():
    main()
