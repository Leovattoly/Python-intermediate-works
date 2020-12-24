# importing required modules 
import argparse 
from cryptography.fernet import Fernet

def generate_key():
    """
    Creating a new key and saving to a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
     Loading the previous key
    """
    return open("secret.key", "rb").read()

def encrypt_message(message):
    """
     Message encrypting 
    """
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)

    return(encrypted_message)
  
def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    print(decrypted_message.decode())

#Creating key 
generate_key()
# create a parser object 
parser = argparse.ArgumentParser(description = "Validating and Encrypting  Reference ID") 
  
# add argument 
parser.add_argument("refid", nargs = 1, metavar = "Reference ID", type = int,help = "reference ID should be 10 digit without any space") 
  
# parse the arguments from standard input 
args = parser.parse_args() 
  
# argument list is converting to string 
strings = [str(integer) for integer in args.refid]
a_string = "".join(strings)

# check if refid argument has numeric input data. 

#If it has, then checking the size of the data 
# Both cases are true then it's showing its valid reference ID 
if a_string.isnumeric() != False and len(a_string) == 10: 
    print(args.refid," is validated succesfully") 
    print("Encrypted ID: ")
    s = encrypt_message(a_string)
    print(s)
    print("Decrypted ID: ")
    decrypt_message(s)
    
else:
    print("Reference id not valid \n")
    