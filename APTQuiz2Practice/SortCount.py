"""
Created on 11/11/2021

@author: alyssa
"""

def occurrences(letter, words):
    '''
    letter is a string of one lowercase alphabetic letter
    words is a list of words
    return a sorted list of the unique words by the number of times
       letter occurs in each word. Break ties alphabetically.
    '''

    return sorted(sorted(set(words)), key = lambda a: a.count(letter))

if __name__ == '__main__':
    print (occurrences("e",["one", "two", "three"]))
