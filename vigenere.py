#!/usr/bin/bash
# author : abdullah oulahyane

import struct
import sys
import os
import time

class Vigenere:
    def __init__(self) -> None:
        if(len(sys.argv)<3):
            self.usage()
        self.chars = [chr(i) for i in range(ord('0'),ord('z')+1)]
        self.key = "mdapetrburg" if len(sys.argv)<=3  else sys.argv[3]
        self.operation = sys.argv[1]
        self.plain = sys.argv[2]

        if len(self.key)<len(self.plain):
            self.cipher = self.key*(len(self.plain)//len(self.key)) + self.key[:(len(self.plain)%len(self.key))]
        else:
            self.cipher = self.key[:len(self.plain)]
        self.run()
        

    def usage(self):
        print(f"Usage:  $ python ./{sys.argv[0]} <enc/dec> <palintext/encryptedtext> <key:optional>")
        exit(-1)

    def print(self,message:str,cipher:str):
        out = ""
        sys.stdout.write(message)
        for s in cipher:
            sys.stdout.flush()
            sys.stdout.write(f"{s}")
            time.sleep(0.01)
        sys.stdout.write("\n")


    def run(self):

        if self.operation.lower() in ["enc","encrypt"]:
            self.encrypt()
        elif self.operation.lower() in ["dec","decrypt"]:

            self.decrypt()

    def encrypt(self):
        output = ""
        for p,k in zip(self.plain,self.cipher):
            if p not in self.chars:
                output+=p
                continue
            pindex = self.chars.index(p)
            kindex = self.chars.index(k)
            rindex = (pindex+kindex) % len(self.chars)
            output+= self.chars[rindex]
        print("Plain: ",self.plain)
        self.print("Encrpyted:  ",output)

    def decrypt(self):
        output = ""
        for p,k in zip(self.plain,self.cipher):
            if p not in self.chars:
                output+=p
                continue
            pindex = self.chars.index(p)
            kindex = self.chars.index(k)
            rindex = (pindex-kindex) % len(self.chars)
            output+= self.chars[rindex]
        print("Plain: ",self.plain)
        self.print("Decrpyted:  ",output)


Vigenere()