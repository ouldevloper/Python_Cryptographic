#!/usr/bin/env python3
# Author : abdullah oulahyane

import os
import sys 
import random



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
        self.encrypt(plain)
        self.decrypt(self.privateKey,self.publicKey,self.outPut)

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

    def encrypt(self,plainText):
        for m in plainText:
            p = random.choice(self.primesNumbers)
            q = random.choice(self.primesNumbers)
            n = p*q
            euler = (p-1)*(q-1)
            for i in range(2,euler):
                if i%
            e = random.choice(range(2,euler))
            C = ( ord(m) ^ e ) % euler
            self.outPut += chr(C)
            self.publicKey.append(e)
            self.privateKey.append(n)
        print("privat Key",self.privateKey)
        print("public Key",self.publicKey)
        print("Encrypted Text : ",self.outPut)


    def decrypt(self,publicKey,cipher):
        for i in range(len(cipher)):
            d = 
            C = 


RSA(input("enter a plain"))