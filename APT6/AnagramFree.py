"""
Created on 11/6/2021

@author: alyssa
"""


def getMaximumSubset(words):
    """
    return int value that represents
    size of largest anagram-free subset
    of values in words, a list of strings
    """

    return len(set(["".join(sorted(w)) for w in words]))

if __name__ == '__main__':
    print (getMaximumSubset(["abcd","abdc","dabc","bacd"]))
