"""
Created on 11/4/2021

@author: alyssa
"""


def sort(data):
    """
    return list of strings based on
    the list of strings in parameter data
    """

    dict = {}
    for fruit in data:
        if fruit not in dict.keys():
            dict[fruit] = 1
        else:
            dict[fruit] += 1
    lst = list(dict.items())
    sortedLst = sorted(lst, key = lambda x: (-x[1], x[0]))
    ret = []
    for i in sortedLst:
        ret.append(i[0])
    return ret

"""
solution by sorting the alphabetical list first, so that
when it sorts by frequency it will already be sorted
alphabetically

def sort1(data):
    data = sorted(data)
    dict = {}
    for fruit in data:
        if fruit not in dict.keys():
            dict[fruit] = 1
        else:
            dict[fruit] += 1
    lst = list(dict.items())
    sortedLst = sorted(lst, key=lambda x: x[1], reverse = True)
    ret = []
    for i in sortedLst:
        ret.append(i[0])
    return ret

"""

if __name__ == '__main__':
    print (sort(["d","c","b","a"]))
