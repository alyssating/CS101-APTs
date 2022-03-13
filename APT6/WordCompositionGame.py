"""
Created on 11/4/2021

@author: alyssa
"""

def score(listA, listB, listC):
    setInAll = set(listA) & set(listB) & set(listC)
    setInTwo = ((set(listA) & set(listB)) | (set(listA) & set(listC)) | (set(listB) & set(listC))) - setInAll
    setInOne = (set(listA) | set(listB) | set(listC)) - (setInAll | setInTwo)

    ret = []
    for lst in [listA, listB, listC]:
        points = len(set(lst) & setInAll) * 1 + len(set(lst) & setInTwo) * 2 + len(set(lst) & setInOne) * 3
        ret.append(points)
    return str(ret[0]) + "/" + str(ret[1]) + "/" + str(ret[-1])

"""
original, lest efficient solution:

def score(listA, listB, listC):
    return String based on three string list parameters
    3 points for each unique word that only he has, 2 points
    for each word that is shared with exactly one other player,
    and 1 point for each word that is shared with both of the other
    players.

    setInAll = set(listA) & set(listB) & set(listC)
    setInTwo = ((set(listA) & set(listB)) | (set(listA) & set(listC)) | (set(listB) & set(listC))) - setInAll
    setInOne = (set(listA) | set(listB) | set(listC)) - (setInAll | setInTwo)

    setPlayerA = set(listA)
    playerAPoints = len(setPlayerA & setInAll) * 1 + len(setPlayerA & setInTwo) * 2 + len(setPlayerA & setInOne) * 3

    setPlayerB = set(listB)
    playerBPoints = len(setPlayerB & setInAll) * 1 + len(setPlayerB & setInTwo) * 2 + len(setPlayerB & setInOne) * 3

    setPlayerC = set(listC)
    playerCPoints = len(setPlayerC & setInAll) * 1 + len(setPlayerC & setInTwo) * 2 + len(setPlayerC & setInOne) * 3

    return str(playerAPoints) + "/" + str(playerBPoints) + "/" + str(playerCPoints)
"""

if __name__ == '__main__':

    print (score(["cat", "dog", "pig", "mouse"],["cat", "pig"],["dog", "cat"]))