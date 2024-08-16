# coding: utf-8
def recursive_integer_conversion(digits):
    length = len(digits)
    def summation(digits, place):
        if len(digits) == 0:
            return int(0)
        elif len(digits) == 1:
            return int(digits[-1])
        else:
            first_part = int(digits[0]) * place
            second_part = int(summation(digits[1:], place / 10))
            return (first_part + second_part)
    return summation(digits, 10 ** (length - 1))
    
