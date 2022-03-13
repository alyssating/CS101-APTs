"""
Created on 11/17/2021

@author: alyssa
"""

def countVisible(trophies):
    """
    return two-element int list
    based on trophies, an int list
    """

    tallest = 0
    count1 = 0
    for i in range(len(trophies)):
        if i == 0:
            count1 += 1
            tallest = trophies[i]
        else:
            if trophies[i] > tallest:
                count1 += 1
                tallest = trophies[i]

    trophies.reverse()

    tallest = 0
    count2 = 0
    for i in range(len(trophies)):
        if i == 0:
            count2 += 1
            tallest = trophies[i]
        else:
            if trophies[i] > tallest:
                count2 += 1
                tallest = trophies[i]

    return [count1, count2]

if __name__ == '__main__':
    print (countVisible([1,4,2,5,3,7,1]))
