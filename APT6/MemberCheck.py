"""
Created on 11/3/2021

@author: alyssa
"""

def whosDishonest(club1, club2, club3):
    """
    return sorted list of Strings, the names
    that appear in more than one of the
    String lists club1, club2, club3
    """

    overlapOneandTwo = set(club1) & set(club2)
    overlapOneandThree = set(club1) & set(club3)
    overlapTwoandThree = set(club2) & set(club3)
    setDishonest = overlapOneandTwo | overlapOneandThree | overlapTwoandThree
    ret = list(setDishonest)
    ret.sort()

    return ret

if __name__ == '__main__':
    print(whosDishonest(["JOHN","JOHN","FRED","PEG"],["PEG","GEORGE"],["GEORGE","DAVID"]))

