from cryptography.fernet import Fernet
message = input('Message -> ')
key = Fernet.generate_key()
fernet = Fernet(key)
enctxt = fernet.encrypt(message.encode())
print(enctxt)
print(key)
