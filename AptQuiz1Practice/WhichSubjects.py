"""
Created on 10/7/2021

@author: alyssa
"""

def inLetters(word):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in word:
        if i not in alphabet:
            return False
    return True

def computeSubjects(phrase):
    '''
    Given the string phrase, return a phrase
    that includes all the words from phrase that do
    not contain a digit or "-" or ":". Those words must
    be in the same order they were in  phrase.
    '''

    list = []
    for word in phrase.split():
        if inLetters(word) == True:
            list.append(word)
    return " ".join(list)

if __name__ == '__main__':
    print (computeSubjects("hello my n-ame i:s 101"))