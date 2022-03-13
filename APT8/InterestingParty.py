"""
Created on 11/22/2021

@author: alyssa ting
"""

def bestInvitation(first, second):
    """
    return int based on string list
    parameters first and second
    """

    lst = [first,second]
    dict = {}
    for x in lst:
        for i in x:
            if i not in dict:
                dict[i] = 0
            dict[i] += 1
    return sorted(dict.items(), key = lambda x: x[1], reverse = True)[0][1]

if __name__ == '__main__':
    print (bestInvitation(["t", "o", "p", "c", "o", "d", "e", "r", "s",
          "i", "n", "g", "l", "e", "r", "o", "u", "n",
          "d", "m", "a", "t", "c", "h", "f", "o", "u",
          "r", "n", "i"],["n", "e", "f", "o", "u", "r", "j", "a", "n",
          "u", "a", "r", "y", "t", "w", "e", "n", "t",
          "y", "t", "w", "o", "s", "a", "t", "u", "r",
          "d", "a", "y"]))
