"""
Created on 10/8/2021

@author: alyssa
"""
import math
lenList = []
def findTarget(phrases):
    for x in range(len(phrases)):
        words = phrases[x].split()
        num = len(words)
        if num > len(phrases):
            return x
    return phrases[len(phrases) - 1]

def lengthList(phrases, targetIndex, targetLength):
    global lenList
    for x in range(len(phrases)):
        if x != targetIndex:
            words = phrases[x].split()
            numWords = len(words)
            difference = numWords - targetLength
            difference = abs(difference)
            lenList.append(difference)
        else:
            lenList.append(0)
    return lenList

def buildlist(phrases):
    '''
    Given the list parameter phrases,
    that contains a list of strings,
    compute the target phrase in the list as the
    first phrase that has more words in it
    than there are phrases in the list. If there is
    no such phrase then the target phrase is the
    last phrase in the list. Return a list of
    integers such that the kth integer in the list
    is the number of words different between the
    kth phrase and the target phrase.
    '''
    #["run dog","the winner of the tournament","beat the curfew", "a pretty red rose grows in the nice garden"]
    targetIndex = findTarget(phrases)
    target = phrases[targetIndex]
    targetWords = target.split()
    targetLength = len(targetWords)
    lenList = lengthList(phrases, targetIndex, targetLength)
    return lenList

if __name__ == '__main__':
    pass
#     phrases = ["run dog","the winner of the tournament","beat the curfew", "a pretty red rose grows in the nice garden"]
#     print(buildlist(phrases))
