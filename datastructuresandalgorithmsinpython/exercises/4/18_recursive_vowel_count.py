# coding: utf-8
def vowels_and_consonants(string, vowel_count, consonant_count):
    vowels = "aeiou"
    if len(string) == 0:
        if vowel_count > consonant_count:
            return True
        else:
            return False
    else:
        if string[0] in vowels:
            vowel_count += 1
            return vowels_and_consonants(string[1:], vowel_count, consonant_count)
        else:
            consonant_count += 1
            return vowels_and_consonants(string[1:], vowel_count, consonant_count)
            
