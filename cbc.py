# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 23:48:54 2018

@author: Avinash
"""

import pyaes
import time

# A 256 bit (32 byte) key
key = "This_key_for_demo_purposes_only!".encode('utf-8')

# For some modes of operation we need a random initialization vector
# of 16 bytes
iv = "InitializationVe"
aes = pyaes.AESModeOfOperationCBC(key, iv = iv)
plaintext = "TextMustBe16Byte"
start_time=time.time()
ciphertext = aes.encrypt(plaintext)
print(time.time()-start_time)

# '\xd6:\x18\xe6\xb1\xb3\xc3\xdc\x87\xdf\xa7|\x08{k\xb6'
print (ciphertext)


# The cipher-block chaining mode of operation maintains state, so
# decryption requires a new instance be created
aes = pyaes.AESModeOfOperationCBC(key, iv = iv)
decrypted = aes.decrypt(ciphertext)

# True
print (decrypted)
