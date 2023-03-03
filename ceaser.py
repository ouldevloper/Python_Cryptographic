#!/usr/bin/env python
# author : abdullah oulahyane

class Ceaser:
    def __init__(self, op,text,key) -> None:
        self.charset = "".join([chr(i) for i in range(ord('A'),ord('Z')+1)])
        self.text = text.upper()
        self.key = key
        self.op = op

    def run(self):
        if self.op == "enc":
            self.encrypt()
        elif self.op == "dec":
            self.decrypt()
        else:
            print("Not supported operation.")
            exit(-1)
    def encrypt(self):
        output = ""
        for char in self.text:
            if char not in self.charset:
                output+= char
            else:
                output += self.charset[(self.charset.index(char)+self.key)%26]

        print("Plain: ",self.text,"\nEncryption : ",output)

    def decrypt(self):
        output = ""
        for char in self.text:
            if char not in self.charset:
                output+= char
            else:
                output += self.charset[(self.charset.index(char)-self.key)%26]
        print("Plain: ",self.text,"\nDecryption : ",output)
        



Ceaser(input("enter opration [enc/dec]: "),input("Enter text: "),int(input("Enter key: "))).run()