"""
Created on 11/13/2021

@author: alyssa ting
"""

def lower(phrase):
    '''
    This function accepts one parameter, phrase, which is a string.

    The function should return the number of lowercase vowels in phrase.
    '''
    lowervowels = "aeiou"
    count = 0
    for word in phrase.split():
        for ch in word:
            if ch in lowervowels:
                count += 1
    return count

if __name__ == '__main__':
    print (lower("Why are you and I still trying to grade?"))
