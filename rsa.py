#!/usr/bin/env python3
# Author : abdullah oulahyane

import os
import sys 
import random
import math


#----------------- RSA Symitric Cryptographic -------------------------
# - key generation
#
# choose 2 Prime Numbers P,Q (3,7)
# Compute n, n = P*Q = (3*7) = 21 
# Compute euler = (p-1)(q-1) = 2*6 = 12
# Choose e , with 1<e<euler and must comprime euler(7) 
#               thats mean euler shouldnt divided by e 
# key is (n,e)  = (21,7)
#
#
# - Message Encryption
#   C = m^e mod n
#   Example emcrypt M = 4 
#   C = 4^7 mode 21 = 16384 % 21 = 4
# - Decrypt Message
#   M = c^d mod n
#   d = e^-1 mod euler
#   d = 7^-1 % 12
#   M = 4^7 %21 = 4
#---------------------------------------------------------------------



class RSA:
    def __init__(self,plain):
        self.primesNumbers = self.getPrimeNumbers()
        self.privateKey = []
        self.publicKey = []
        self.outPut = ""
        self.generationKeys()
        self.encrypt(plain)
        #self.decrypt(self.privateKey,self.publicKey,self.outPut)

    def getPrimeNumbers(self):
        output = [2, 3, 5, 7] #[item for item in range(1024)]
        # output = filter(lambda x : x%)
        for num in range(10,1024+1):
            tmp = 0
            for i in range(2,10):
                if num % i == 0:
                    tmp+=1
            if tmp == 0:
                output.append(num)
        return output

    def generationKeys(self):
        p = random.choice(self.primesNumbers)
        q = random.choice(self.primesNumbers)
        n = p*q
        euler = (p-1)*(q-1)
        e = list(filter(lambda x : math.gcd(x,euler) == 1 ,range(2,euler)))[0]
        self.publicKey = (e,euler)
        d = 2
        while 1:
            if (d*e)%euler:
                break
            d+=1
        self.privateKey = (d,euler)


    def encrypt(self,plainText):
        publicKey,euler = self.publicKey
        output = ""
        for m in plainText:
            C = math.pow( ord(m) , publicKey )  % euler
            output += chr(int(C))

        print("public Key",publicKey)
        print("Encrypted Text : ",output.encode().hex())


    def decrypt(self,publicKey,cipher):
        publicKey = self.publicKey

        for i in range(len(cipher)):
            pass
            # d = 
            # C = 


RSA(input("enter a plain"))