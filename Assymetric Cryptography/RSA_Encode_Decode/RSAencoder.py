from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization


def encrypt(nameFileIn, nameFileOut, key):

    msg = readFile(nameFileIn, 'br')

    encrypted = key.encrypt(msg,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
    
    writeToFile(nameFileOut,encrypted)

    




def readFile(nameFile, mode):
    File = open(nameFile, mode)
    text = File.read()
    return text



def writeToFile(nameFile,content):

    try:
        File = open(nameFile, 'xb')
    except FileExistsError:
        File = open(nameFile, 'wb')  

    File.write(content)



def keyLoad(keyFile):

    with open(keyFile, "rb") as key_file:
        publicKey= serialization.load_pem_public_key(key_file.read())
      
    return publicKey






def main():   

  #nameFileIn, nameFileOut = input("What file do you want to encrypt and where do you want to store the output.\n").split()
  
  #keyFile = input("Name of file with the key")"

    #testing
    nameFileIn = "text.txt"
    nameFileOut = "textEncodedv2.txt"
    keyFile = "keypub.pem"

    
    public_key = keyLoad(keyFile)
    encrypt(nameFileIn, nameFileOut, public_key)
    
    
if __name__ == main():
    main()

