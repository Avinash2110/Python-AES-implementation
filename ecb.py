# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 20:28:18 2018

@author: Avinash
"""
import pyaes
import time

key = "This_key_for_demo_purposes_only!".encode("utf-8")
aes = pyaes.AESModeOfOperationECB(key)
plaintext = "TextMustBe16Byte"
start_time=time.time()
ciphertext = aes.encrypt(plaintext)
print(time.time()-start_time)

# 'L6\x95\x85\xe4\xd9\xf1\x8a\xfb\xe5\x94X\x80|\x19\xc3'
print (ciphertext)

# Since there is no state stored in this mode of operation, it
# is not necessary to create a new aes object for decryption.
#aes = pyaes.AESModeOfOperationECB(key)
decrypted = aes.decrypt(ciphertext)

# True
print (decrypted)
