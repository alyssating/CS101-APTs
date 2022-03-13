"""
Created on 11/11/2021

@author: alyssa
"""

def popular(phrase):
    '''
    phrase is a string of words
    Return the sorted list of unique words that have the most
        popular 3-character ending. Only consider words of length
        3 or more. Duplicate words only count once. Break ties with
        the 3-character ending that comes last in alphabetical order.
    '''

    dict = {}
    for word in list(set(phrase.split())):
        if len(word) >= 3:
            ending = word[-3:]
            if ending not in dict:
                dict[ending] = 0
            dict[ending] += 1
    lst = sorted(sorted(dict.items(), reverse = True),key = lambda x: -x[1])
    if len(lst) > 0:
        popEnding = lst[0][0]
        ret = []
        for word in phrase.split():
            if word[-3:] == popEnding and word not in ret:
                ret.append(word)
        return sorted(ret)
    return []

# phrase = "jingle bells in a single line"

if __name__ == '__main__':
    print (popular("a b c d go"))