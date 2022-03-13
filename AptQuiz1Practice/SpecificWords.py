"""
Created on 10/5/2021

@author: alyssa
"""


def countwords(phrase, ending, item):
    '''
    Given the three string parameters
    phrase, ending and item,
    return the number of words in phrase
    that end in ending and do not contain
    item as part of their word.
    '''

    list = phrase.split()

    list2 = []
    for i in list:
        if ending in i:
            list2.append(i)

    list3 = []
    for j in list2:
        if item not in j:
            list3.append(j)

    return len(list3)


if __name__ == '__main__':
    print(countwords("swim trim shop drop swap rim", "im", "sh"))
