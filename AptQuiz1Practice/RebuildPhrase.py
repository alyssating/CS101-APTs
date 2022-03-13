"""
Created on 10/8/2021

@author: alyssa
"""

def adjustPhrase(phrase, letter):
    '''
    Given the string parameter phrase,
    and the parameter letter,
    return a copy of the phrase modified such that
    for any word that does not start with letter but has
    letter in it, that word is changed to be only those
    letters in the word up to the first occurrence of letter.
    '''

    list = []
    for i in phrase.split():
        if i.find(letter) == 0:
            list.append(i)
        elif i.find(letter) > -1:
            index = i.find(letter)
            list.append(i[:index])
        else:
            list.append(i)

    return " ".join(list)

if __name__ == '__main__':
    print (adjustPhrase("this is a test", "s"))
