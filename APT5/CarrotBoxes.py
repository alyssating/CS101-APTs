"""
Created on 10/27/2021

@author: alyssa
"""

def theIndex(carrots,amount):
    max = 0
    index = 0
    amountToEat = amount
    while amountToEat > 0:
        for x in range(len(carrots)):
            if carrots[x] > max:
                max = carrots[x]
                index = x
        carrots[index] -= 1
        amountToEat -= 1
        max = 0
    return index

"""
more efficient function:

def theIndex(carrots,amount):
    boxIndex = 0
    for aCarrot in range(amount):
        boxIndex = carrots.index(max(carrots))
        carrots[boxIndex] -= 1
    return boxIndex
"""
if __name__ == '__main__':
    print (theIndex([14,36,52,86,27,97,3,67],300))
