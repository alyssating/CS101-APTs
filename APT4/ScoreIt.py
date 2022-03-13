"""
Created on 10/12/2021

@author: alyssa
"""


def maxPoints(toss):
    """
    return int representing the maximal Yahtzee
    score based on rolls in integer list toss
    """

    sumOnes = toss.count(1) * 1
    sumTwos = toss.count(2) * 2
    sumThrees = toss.count(3) * 3
    sumFours = toss.count(4) * 4
    sumFives = toss.count(5) * 5
    sumSixes = toss.count(6) * 6

    sumsList = [sumOnes,sumTwos,sumThrees,sumFours,sumFives,sumSixes]

    sumMax = [sum for sum in sumsList if sum == max(sumsList)]

    return sumMax[0]

if __name__ == '__main__':
    pass