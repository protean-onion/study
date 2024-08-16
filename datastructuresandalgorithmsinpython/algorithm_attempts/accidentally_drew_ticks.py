# coding: utf-8
def recursive_integer_conversion(digits):
    length = len(digits)
    def summation(digits, power):
        if len(digits) == 1:
            print("Returning: " + str(int(digits[0])))
            return int(digits[0])
        else:
            print("Returning: " +  str((int(digits[0]) * power) + summation(digits[1:], power / 10)))
            return (int(digits[0]) * power) + summation(digits[1:], power / 10)
    summation(digits, 10 ** (length - 1))
    
