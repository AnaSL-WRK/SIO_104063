
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

KEY_SIZE_OPTIONS = ['1024','2048','3072', '4096']


def keyGen(namePub,namePriv,size):
    
    key = rsa.generate_private_key(public_exponent=65537,key_size=size)


    pemPriv = key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.TraditionalOpenSSL,encryption_algorithm=serialization.NoEncryption())

    #privK = pemPriv.splitlines()[0]
    writeToFile(namePriv,pemPriv)

    public_key = key.public_key()
    pemPub = public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)

    #pubK = pemPub.splitlines()[0]
    writeToFile(namePub,pemPub)



def writeToFile(nameFile,content):

    try:
        File = open(nameFile, 'xb')
    except FileExistsError:
        File = open(nameFile, 'wb')  

    File.write(content)




def main():   

  #namepub, namepriv= input("What name do you want to give your public key and your private key.\n").split()
  
  #size = input("What size do you want the key to be? (1024,2048,3072,4096")


  #if size not in KEY_SIZE_OPTIONS:
  #      print("Error! Invalid size specified \n")
  #      print("Sizes allowed: ")
  #      print("1024, 2048, 3072, 4096")
  #      exit(1)
    #testing
    namepub = "keypub.pem"
    namepriv = "keypriv.pem"
    size = 2048

    

    keyGen(namepub,namepriv,size)
    
    
if __name__ == main():
    main()

