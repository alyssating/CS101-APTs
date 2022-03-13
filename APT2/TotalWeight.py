"""
Created on 9/27/2021

@author: alyssa
"""

def weight3(ab, ac, bc):
    """
    return float indicating
    the total amount of weight for objects a, b and c.
    You are given the combined weight of a and b
    together as parameter ab, the combined weight of
    a and c together as parameter ac,
    and the weight of b and c together with parameter bc.
    """

    if bc > ab and ac:
        weightCminusA = bc - ab
        weightC = (weightCminusA + ac) / 2
        weightB = bc - weightC
        weightA = ab - weightB

        return weightA + weightB + weightC

    if ab > ac and bc:
        weightBminusC = ab - ac
        weightB = (weightBminusC + bc) / 2
        weightA = ab - weightB
        weightC = ac - weightA

        return weightA + weightB + weightC

    else:
        weightCminusB = ac - ab
        weightC = (weightCminusB + bc) / 2
        weightA = ac - weightC
        weightB = ab - weightC

        return weightA + weightB + weightC

if __name__ == '__main__':
    pass