"""
Created on 10/8/2021

@author: alyssa
"""
def differentvowels(word):
    vowels = "aeiou"
    counter = 0
    for char in word:
        if char in vowels:
            vowels = vowels.replace(char, "")
            counter += 1
    return counter

def countwords(phrase):
    '''
    Given the string parameter phrase,
    return the number of words in phrase
    that have exactly two different vowels
    as part of their word.
    '''

    list = []
    for word in phrase.split():
        if differentvowels(word) == 2:
                list.append(word)
    return len(list)

if __name__ == '__main__':
    print (countwords("hello my name is alyssa this is finished"))
