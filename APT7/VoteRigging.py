"""
Created on 11/17/2021

@author: alyssa
"""


def minimumVotes(votes):
    """
    returns minimum number of votes(int) to change
    using values in votes (integer list)
    """
    count = 0
    dex = 0
    if len(votes) > 1:
        while votes[0] <= max(votes[1:]):
            for x in range(len(votes)):
                if votes[x] >= max(votes):
                    dex = x
            votes[dex] -= 1
            votes[0] += 1
            count += 1

        return count
    return 0
if __name__ == '__main__':
    print (minimumVotes([10]))
