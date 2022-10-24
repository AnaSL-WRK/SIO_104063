from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def encrypt(nameFileIn, nameFileOut, keyFile):

    msg = readFile(nameFileIn, 'r')
    key = readFile(keyFile, 'b')


    ciphertext = key.encrypt(msg,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
    












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




def main():   

  #nameFileIn, nameFileOut = input("What file do you want to encrypt and where do you want to store the output.\n").split()
  
  #keyFile = input("Name of file with the key")"

    #testing
    nameFileIn = "text.txt"
    nameFileOut = "textEncoded.txt"
    keyFile = "keypub.pem"

    

    encrypt(nameFileIn, nameFileOut, keyFile)
    
    
if __name__ == main():
    main()

