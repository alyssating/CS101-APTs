"""
Created on 11/13/2021

@author: alyssa ting
"""


def sortReverse(phrase):
    '''
    The string parameter phrase is a string of one or
    more words or combinations of words, numbers, and
    symbols.

    The function should return a reverse sorted list of the
    words in the string.
    '''

    return sorted(phrase.split(),reverse = True)

if __name__ == '__main__':
    print (sortReverse("This is a tester string."))
