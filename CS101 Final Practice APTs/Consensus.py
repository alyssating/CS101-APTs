"""
Created on 12/10/2021

@author: alyssa
"""


def majorityWinner(voteA, voteB, voteC):
    '''
    voteA (int) - Number of votes received by candidate A
    voteB (int) - Number of votes received by candidate B
    voteC (int) - Number of votes received by candidate C

    Returns a string representing which candidate won the majority vote, based
    on the three parameters. If there is no majority winner, return "No one".
    '''

    votesNeeded = (voteA + voteB + voteC) / 2

    if voteA > votesNeeded:
        return "A"
    elif voteB > votesNeeded:
        return "B"
    elif voteC > votesNeeded:
        return "C"
    return "No one"

if __name__ == '__main__':
    voteA = 5
    voteB = 4
    voteC = 1
    print (majorityWinner(voteA,voteB,voteC))
