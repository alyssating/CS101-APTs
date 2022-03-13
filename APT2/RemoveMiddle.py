"""
Created on 9/26/2021

@author: alyssa
"""

def shorten(name):
    """
    return the name with the middle name(s) removed.
    name has at least one word.
    """

    nameList = name.split()
    length = len(nameList)

    if length == 1:
        return nameList[0]

    else:
        firstName = nameList[0]
        lastName = nameList [-1]

        return str(firstName) + " " + str(lastName)

if __name__ == '__main__':
    pass
