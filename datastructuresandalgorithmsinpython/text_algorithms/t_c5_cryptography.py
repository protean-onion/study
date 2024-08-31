class CaesarCipher:
    def __init__(self, rotation_value):
        self.rotation_value = rotation_value

    def encrypt(self, string):
        return "".join([chr((ord(letter) + self.rotation_value - 64) % 26 + 64) for letter in list(string)])

    def decipher(self, encrypted_string):
        return "".join([chr((ord(letter) - self.rotation_value - 64) % 26 + 64) for letter in list(encrypted_string)])