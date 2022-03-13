"""
Created on 9/30/2021

@author: alyssa
"""


def bagelCount(orders):
    """
    return number of bagels needed to fulfill
    the orders in integer list parameter orders
    """

    total = 0
    for i in range(len(orders)):
        if orders[i] >= 12:
            dozens = orders[i] // 12
            total = total + orders[i] + dozens

        else:
            total = total + orders[i]

    return total

if __name__ == '__main__':
    print(bagelCount([1,3,5,7]))