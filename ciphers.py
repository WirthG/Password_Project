# Ignore this file!
def encrypt_caesar(message):
    numbers = []
    words = message.split()
    for i in words:
        # Changing the symbols to minus 4
        number = ord(i) - 4
        numbers.append(ord(number)) # Individual Characters
    print (numbers)

def decrypt_caesar(self, message):
    pass

message = input("Enter the message you would like to encrypt: ")
encrypt_caesar(message)