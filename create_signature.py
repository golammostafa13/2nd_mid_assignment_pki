from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

#import codecs


message = b'The user public key = "10201", the user is vaccinated'
key = RSA.import_key(open('private.key').read())
h = SHA256.new(message)

'''
once hashing is done, we need to create a sign object through 
which we can sign a message
'''

signer=pkcs1_15.new(key)
signature=signer.sign(h)
#signature = pkcs1_15.new(key).sign(h)
#signature_readable=codecs.getencoder('hex')(signature)
print(signature.encode('hex'))


file_out = open("signature.pem", "wb")
file_out.write(signature)
file_out.close()

file_out = open("message.txt", "wb")
file_out.write(message)
file_out.close()
