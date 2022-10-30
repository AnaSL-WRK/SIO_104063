from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization


def encrypt(nameFileIn, nameFileOut, key):

    msg = readFile(nameFileIn, 'br')

    decripted = key.decrypt(msg,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
    
    writeToFile(nameFileOut,decripted)

    




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
        private_key = serialization.load_pem_private_key(key_file.read(),password=None)
      
    return private_key






def main():   

  #nameFileIn, nameFileOut = input("What file do you want to decrypt and where do you want to store the output.\n").split()
  
  #keyFile = input("Name of file with the key")"

    #testing
    nameFileIn = "textEncoded.txt"
    nameFileOut = "textDecoded.txt"
    keyFile = "keypriv.pem"

    
    private_key = keyLoad(keyFile)
    encrypt(nameFileIn, nameFileOut, private_key)
    
    
if __name__ == main():
    main()

