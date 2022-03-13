"""
Created on 10/9/2021

@author: alyssa ting
"""


def findString(input):
    '''
    The string parameter input is comprised of one or
    more words or combinations of words, numbers, and
    symbols.

    The function should return the number of words in
    the string that end with a vowel.
    '''

    list = []
    vowels = "aeiouAEIOU"
    for word in input.split():
        if word[-1] in vowels:
            list.append(word)
    return len(list)

if __name__ == '__main__':
    pass