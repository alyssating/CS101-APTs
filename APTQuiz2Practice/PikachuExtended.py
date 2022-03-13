"""
Created on 11/13/2021

@author: alyssa
"""

def check(word):
    '''
    word (str) - A string Pikachu may or may not be able to say

    Return whether Pikachu can say this word. If it can return "YES",
    if it can't return "NO".
    '''

    p = word.find("p")
    c = word.find("c")
    k = word.find("k")

    dexList1 = [p,c,k]
    dexList2 = []
    for dex in dexList1:
        if dex >= 0:
            dexList2.append(dex)
    lst = sorted(dexList2)

    ret = []
    for i in range (len(lst)):
        if i == len(lst)-1:
            ret.append(word[lst[i]:])
        else:
            ret.append(word[lst[i]:lst[i+1]])

    ret2 = []
    for i in ret:
        ret2.append("".join(list(set(i))))

    count = 0
    for i in ret2:
        if len(set(i) ^ {'p', 'i'}) == 0:
            count += 1
        elif len(set(i) ^ {'k', 'a'}) == 0:
            count += 1
        elif len(set(i) ^ {'c', 'h', 'u'}) == 0:
            count += 1
        else:
            count += 0
    if count == len(ret2):
        return "YES"
    return "NO"

if __name__ == '__main__':
    print (check("chuuuuuka"))
