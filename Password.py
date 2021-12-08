from cryptography.fernet import Fernet
from secretmessage import secretmessage

class password:
    # This will eventually be its own class in a different file.
    print("Welcome to the message encryption machine")
    print("------------------------------------------------")
    response = input("Would you like to encrypt a message? (Y/N) ")
    if (response == "N"):
        print ("Thats alright, have a nice day!")
    elif (response == "Y"):
        generate_key()
        read_key()
        encrypt_message()
        password = input("What password would you like to use for your message?")
        print ("Your password,", password, "has been set! Only this password will be able to decrypt your message!")
        ask = input("Type your password to decrypt your message: ")
        if (ask == password):
            decrypt_message()
        else:
            print("Incorrect Password!")