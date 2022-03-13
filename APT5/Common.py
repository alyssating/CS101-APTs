"""
Created on 10/28/2021

@author: alyssa
"""

def count(a,b):
    listA = list(a)
    listB = list(b)
    inCommon = 0
    for char in listA:
        if char in listB:
            inCommon += 1
            listB.remove(char)
    return inCommon

if __name__ == '__main__':
    print (count("horse", "mirth"))
