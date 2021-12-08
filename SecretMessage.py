import time
from cryptography.fernet import Fernet

def generate_key():
        # Creates a Key
    key = Fernet.generate_key()
    #Opens the file and writes down the Key
    file = open('key.key', 'wb')
    file.write(key) #Key is type bytes
    file.close()

def read_key():
    #Globalize our Variable, key
    global key
    #Reads the file with our key inside of it
    file = open("key.key", "rb")
    key = file.read() #Key is type bytes
    file.close()


def encrypt_message():
    #key = read_key() ---- This is another option instead of globalization
    global encrypted_message
    message = input("Write a message you would like to encrypt: ") #Take user input for message
    start_time = time.time()
    encoded_message = message.encode() #Turn the stirng into Bytes
    hash1 = Fernet(key)
    encrypted_message = hash1.encrypt(encoded_message) # Assign all of this to encrypted_message
    end_time = time.time()
    print("Symmetrically encypting your message took this long: {}".format(round((end_time-start_time),5)))
    print(f"\nThis is what your message looks like now: {encrypted_message}\n This is called cipher text!")

# Decryption Section
def decrypt_message():
    start_time = time.time()
    hash2 = Fernet(key)
    decrypted_message = hash2.decrypt(encrypted_message)
    decoded_message = (decrypted_message.decode())
    end_time = time.time()
    print("Symmetrically decypting your message took this long: {}".format(round((end_time-start_time),5)))
    print (f"\nThis is your message: {decoded_message}")

#Exocutes all of the functions under one function
def initializeEncrypt():
    generate_key()
    read_key()
    encrypt_message()


# Creates the Formating for the program
print(f"\nWelcome to the message encryption machine")
print(f"------------------------------------------------")
response = input("Would you like to encrypt a message? (Y/N) ")
if (response == "N"):
    print (f"\nThats alright, have a nice day!")
elif (response == "Y"):
    #Runs the encyption part of the program
    initializeEncrypt()
    password = input(f"\nWhat password would you like to use for your message? ")
    #Allows the user to set a password in order to access the decryption method
    print (f"\nYour password,", password, "has been set! Only this password will be able to decrypt your message!")
    ask = input(f"Type your password to decrypt your message: ")
    # If the password is correct, decrypt the message.
    if (ask == password):
        decrypt_message()
    #If the password isn't correct, tell the user it is not correct.
    else:
        print(f"\nIncorrect Password!")