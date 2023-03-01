#!/usr/bin/env python3
import sys
import os
import optparse
import time

class Ceaser:
    def __init__(self):
        self.options = self.getOptions();
        self.charset = "".join([chr(i) for i in range(ord('A'),ord('Z')+1)])
    
    def getOptions(self):
        parse = optparse.OptionParser(f"Usage: $python {sys.argv[0]}  ...args ")
        parse.add_option('-p',dest='OPERATION',type='string',help='specify the operation ex. enc / dec') 
        parse.add_option('-t',dest='TEXT',type='string',help='specify the palin or encrypted text') 
        parse.add_option('-k',dest='KEY',type='int',help='specify the key')

        (options,args) = parse.parse_args()
        if not options.OPERATION or not options.TEXT or not options.KEY:
            print(parse.usage)
            exit(-1)        
        return (options)

    def run(self):
        match self.options.OPERATION:
            case "enc":
                self.encrypt()
                return
            case "dec":
                self.decrypt()
                return
            case _:
                print("operation not found ")
                exit(-1)

    def print(self,text):
        for i in text:
            sys.stdout.write(f"{i}")
            sys.stdout.flush()
            time.sleep(0.01)

    def encrypt(self):
        plain = self.options.TEXT.upper()
        key   = self.options.KEY
        output = "Encrypted Text : "
        for char in plain:
            if char not in self.charset:
                output+=char
            else:
                output += self.charset[(self.charset.index(char)+key)%26]
        self.print("Plain Text     : "+plain+"\n")
        self.print(output)

    def decrypt(self):
        plain = self.options.TEXT.upper()
        key   = self.options.KEY
        output = "Decrypted Text : "
        for char in plain:
            if char not in self.charset:
                output+=char
            else:
                output += self.charset[(self.charset.index(char)-key)%26]
        self.print("Encrypted Text : "+plain+"\n")
        self.print(output)

    

Ceaser().run()