# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 20:03:28 2018

@author: Avinash
"""
import pyaes
import time
import matplotlib.pyplot as plt

Time_list=[]
Size_list=[]
Total_file=int(input('Enter the total files:'))
for i in range(Total_file):
    key = "This_key_for_demo_purposes_only!".encode("utf-8")
    aes = pyaes.AESModeOfOperationCTR(key)
    file_name=input('Enter the name of the file:')
    file_size=int(input('Enter the file size:'))
    f=open(file_name,'rb')
    plaintext=f.read()
    start_time=time.clock()
    ciphertext = aes.encrypt(plaintext)
    encrypt_time=(time.clock()-start_time)
    print(encrypt_time)
    Time_list.append(encrypt_time)
    Size_list.append(file_size)

# '''\xb6\x99\x10=\xa4\x96\x88\xd1\x89\x1co\xe6\x1d\xef;\x11\x03\xe3\xee
#    \xa9V?wY\xbfe\xcdO\xe3\xdf\x9dV\x19\xe5\x8dk\x9fh\xb87>\xdb\xa3\xd6
#    \x86\xf4\xbd\xb0\x97\xf1\t\x02\xe9 \xed'''
    print(ciphertext)

# The counter mode of operation maintains state, so decryption requires
# a new instance be created
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted = aes.decrypt(ciphertext)

# True
    print (decrypted)

# To use a custom initial value
    counter = pyaes.Counter(initial_value = 100)
    aes = pyaes.AESModeOfOperationCTR(key, counter = counter)
    ciphertext = aes.encrypt(plaintext)

# '''WZ\x844\x02\xbfoY\x1f\x12\xa6\xce\x03\x82Ei)\xf6\x97mX\x86\xe3\x9d
#    _1\xdd\xbd\x87\xb5\xccEM_4\x01$\xa6\x81\x0b\xd5\x04\xd7Al\x07\xe5
#    \xb2\x0e\\\x0f\x00\x13,\x07'''
    print (ciphertext)

    f.close()
    running=False
plt.plot(Time_list,Size_list)
plt.title('Graph between file size and encryption time')
plt.ylabel('file size')
plt.xlabel('encryption time')
plt.grid(True,color='k')
plt.show()

plt.bar(Time_list,Size_list,align='center')
plt.title('Graph between file size and encryption time')
plt.ylabel('file size')
plt.xlabel('encryption time')
plt.show()

plt.scatter(Time_list,Size_list)
plt.title('Graph between file size and encryption time')
plt.ylabel('file size')
plt.xlabel('encryption time')
plt.show()

