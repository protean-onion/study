class CaesarCipher:
    def __init__(self, rotation_value):
        self._construct_schematic(rotation_value)
    
    
    def _construct_schematic(self, rotation_value):
        letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") 

        self.encryption_dictionary = {}
        self.decryption_dictionary = {}

        def generate_decryption_ord(char, rotation_value):
            return_ord = ord(char) - rotation_value

            if return_ord < ord("A"):
                return return_ord + 26
            else:
                return return_ord
        
        def generate_encryption_ord(char, rotation_value):
            return_ord = ord(char) + rotation_value

            if return_ord > ord("Z"):
                return return_ord - 26
            else:
                return return_ord
        

        for letter in letters:
            self.decryption_dictionary[letter] = chr(generate_decryption_ord(letter, rotation_value))
            self.encryption_dictionary[letter] = chr(generate_encryption_ord(letter, rotation_value))

    def encrypt(self, string):
        return "".join([self.encryption_dictionary[letter] for letter in list(string)])
    
    def decipher(self, encrypted_string):
        return "".join([self.decryption_dictionary[letter] for letter in list(encrypted_string)])