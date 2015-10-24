from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
print "Key "+str(cipher_suite)
cipher_text = cipher_suite.encrypt("Secret message")
plain_text = cipher_suite.decrypt(cipher_text)
print "Cipher text "+cipher_text
print "Plain text "+plain_text