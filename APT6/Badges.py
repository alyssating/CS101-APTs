"""
Created on 11/3/2021

@author: alyssa
"""

def findLabel(labels, deeds, needs):
    """
    return string based on parameters
    labels a list of strings
    deeds a list of strings
    and needs a list of strings
    """

    ret = []
    for i in range(len(labels)):
        setNeeds = set(needs[i].split())
        setDeeds = set(deeds)
        overlap = setNeeds & setDeeds
        if len(overlap) == len(setNeeds):
            ret.append(labels[i])
    if len(ret) > 0:
        return ret[0]
    else:
        return "nobadge"

"""
more efficient solution:
def findLabel(labels, deeds, needs):
    for i in range(len(needs)):
        setNeeds = set(needs[i].split())
        if setNeeds.issubset(deeds):
            return labels[i]
    return "no badge"
"""

if __name__ == '__main__':
    print (findLabel(['wolf', 'bear', 'lion'],["fire", "camping", "spanish"],["fire knots camping", "spanish fire internet", "fire camping spanish"]))