"""
Created on 11/4/2021

@author: alyssa
"""


def freqs(data):
    """
    return list of int values corresponding
    to frequencies of strings in data, a list
    of strings
    """

    dict = {}
    for fruit in data:
        if fruit not in dict.keys():
            dict[fruit] = 1
        else:
            dict[fruit] += 1
    lst = list(dict.items())
    lst.sort()
    ret = []
    for i in lst:
        ret.append(i[-1])
    return ret

if __name__ == '__main__':
    print (freqs(["apple", "pear", "cherry", "apple", "cherry", "pear", "apple", "banana"]))
