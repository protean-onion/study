class Cipher:
    def __init__(self, rotation_value):
        self.forward = "".join([chr((i + rotation_value) % 26 + ord("A"))for i in range(0, 26)])
        self.backward = "".join([chr((i - rotation_value) % 26 + ord("A"))for i in range(0, 26)])

    def encrypt(self, string):
        encrypted = []
        for letter in string:
            if letter.isupper():
                print("Letter: " + str(ord(letter)))
                print("A: " + str(ord("A")))
                encrypted.append(self.forward[ord(letter) - ord("A")])
                continue
            else:
                encrypted.append(letter)
        return "".join(encrypted)
    
    def decipher(self, string):
        decrypted = []
        for letter in string:
            if letter.isupper():
                print("Letter: " + str(ord(letter)))
                print("A: " + str(ord("A")))
                decrypted.append(self.backward[ord(letter) - ord("A")])
            else:
                decrypted.append(letter)
        return "".join(decrypted)