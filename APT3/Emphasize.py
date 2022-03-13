"""
Created on 10/4/2021

@author: alyss
"""
def repeat(word, number):
    """
    return the word with the first part of it repeated
    if it is a valid part to repeat. The part to be
    repeated must be repeated "number" times.
    If the first letter is not a vowel, and the third
    letter is a vowel, then the part to repeat is the
    first three letters.
    If the first and third letters are not vowels, but
    the second letter is, then the part to repeat is
    the first two letters.
    Otherwise there is nothing to repeat.
    Only the first letter of the returned word may be
    a capital letter, if the original word started with
    a capital letter.
    """
    vowels = "aeiouAEIOU"
    if (word[0] in vowels) or (len(word) >= 3 and word[0] not in vowels and word[1] not in vowels
                               and word[2] not in vowels) or (len(word) == 1) or \
            (len(word) == 2 and word[1] not in vowels):
        return word
    else:
        if len(word) > 2 and word[2] in vowels:
            if word[0].isupper():
                word = word[:3] * number + word[3:]
                word = word.lower()
                word = word[0].upper() + word[1:]
                return word
            else:
                word = word[:3] * number + word[3:]
            return word
        elif word[1] in vowels:
            if word[0].isupper():
                word = word[:2] * number + word[2:]
                word = word.lower()
                word = word[0].upper() + word[1:]
                return word
            else:
                word = word[:2] * number + word[2:]
            return word

if __name__ == '__main__':
    print (repeat("hi",3))
