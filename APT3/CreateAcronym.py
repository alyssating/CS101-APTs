"""
Created on 10/4/2021

@author: alyssa
"""

def acronym(phrase):
    """
    phrase is a string, zero or more spaces
    return a string: acronym of the string
    parameter phrase
    """

    # list = phrase.split()
    #
    # word = ""
    # for i in list:
    #     word += i[0][0]
    # return word

    # recursion solution:
    phrase = phrase.split()
    if len(phrase) == 1:
        return phrase[0][0]
    return phrase[0][0] + acronym(" ".join(phrase[1:]))

if __name__ == '__main__':
    print (acronym("hello my name"))