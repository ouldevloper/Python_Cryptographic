import ctypes

class Xor:
    def __init__(self,op,data) -> None:
        self.privatekey = "sd,jahgsdgGHJGKHJ658376415283764578^%*&^$#*&^^&*#&^$#*%&^$*%^#$"
        self.operation  = op
        self.data       = data

    def encrypt(self,data):
        output = ""
        for char in data:
            tmp = char
            for key in self.privatekey:
                tmp = chr(ord(tmp) ^ ord(key))
            output+=tmp
        print(f"Encrypted Data : {output.encode().hex()}")

    def decrypt(self,data):
        data = bytes.fromhex(data.replace("0x",""))

        output = ""
        for char in data:
            tmp = chr(char)
            for key in self.privatekey:
                if  ctypes.c_int(char):
                    tmp = chr(ord(tmp) ^ ord(key))
                else:
                    tmp = chr(ord(chr(tmp)) ^ ord(key))

            output+=tmp
        print(f"Decrypted Data : {output}")


    def run(self):
        if self.operation == "enc":
            print("Encrypting Data...")
            self.encrypt(self.data)
        if self.operation == "dec":
            print("Decrypting Data...")
            self.decrypt(self.data)

Xor(input("Enter Operation: [enc/dec]:"),input("Enter Data: [hex format]")).run()