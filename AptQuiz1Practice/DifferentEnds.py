"""
Created on 10/8/2021

@author: alyssa
"""

def countVowelWords(phrase):
    '''
    Given a string parameter
    phrase, return the number of words
    in phrase that start with and end with
    a different vowel.
    '''

    vowels = "aeiouAEIOU"
    list = []
    for i in phrase.split():
        if (i[0] in vowels and i[-1] in vowels) and (i[0] != i[-1]):
            list.append(i)

    return len(list)
if __name__ == '__main__':
    print (countVowelWords("eva anita ellie olga erica uma ida emma irene aimee"))
