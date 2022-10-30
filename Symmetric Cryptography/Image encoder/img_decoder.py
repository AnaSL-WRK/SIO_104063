
import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


def decrypt(nameIn,nameOut,key,iv,encMode):

    file = open( "key.key", 'br')
    key = file.read()

    #if iv != None:
    #    ivRead = open(nameIn, "br") # opening for [r]eading as [b]inary
    #    iv = ivRead.read(16) # if you only wanted to read 512 bytes, do .read(512)

    file = open(encMode, "r")
    file = file.read()
    alg = file.split('\n', 1)[0]

    try: 
        mode = file.split('\n', 1)[1]
    except IndexError:
        mode = None


    img = open(nameIn, "rb")
    dataIn = img.read()
    writeToFile("openAsrb",dataIn)

       

    iv = secrets.token_bytes(16)

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

    dec = decryptor.update(dataIn) + decryptor.finalize()

    unpadded_data = unpadder.update(dec) + unpadder.finalize()


    writeToFile(nameOut,unpadded_data)




def writeToFile(nameFile,content):

    try:
        File = open(nameFile, 'xb')
    except FileExistsError:
        File = open(nameFile, 'wb')  

    File.write(content)





def main():   

   #nameIn, nameOut, key = input("Write what file to decrypt, where you want the output and the key to decrypt \n").split()
   #
   #ans = input("do you have the Iv? [Y/N] ")
   #ans = ans.lower()
#
   #if ans == "y":
   #    iv = input("Paste the Iv string here  \n")
   #else:
   #    iv = None
#
   #ans = input("Do you have the encryption mode? [Y/N] ")
   #ans = ans.lower()
#
   #if ans == "y":
   #    encMode = input("In what file do you have that information ")
   #else: 
   #    print("You need to know the encoding algorithm and mode in order to decode")
#



    #testing
    nameIn = "ecbTux.bmp"
    nameOut = "decrp.bmp"
    key = "key.key"
    iv = "y"
    encMode = "algorithm.txt"

    decrypt(nameIn, nameOut, key, iv, encMode)
    
    
if __name__ == main():
    main()
