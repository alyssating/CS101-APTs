"""
Created on 11/11/2021

@author: alyssa
"""

def sortit(letter, words):
    '''
    letter is a string of one lowercase alphabetic letter
    words is a list of words
    return a sorted list of the unique words that
        do not start with letter
    '''

    lst = []
    ret = []
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for word in words:
        for ch in list(word):
            if ch in alphabet:
                lst.append(word) #appending only words that are made up of letters
    for word in list(set(lst)):
        if word[0] != letter:
            ret.append(word)
    return sorted(ret)

if __name__ == '__main__':
    print (sortit("p", ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'xx', 'xx', 'xx', 'y', '*', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'o', 'o', 'o', 'o', 'o', 'oo', 'oo', 'oo', 'oo', 'oo']))
