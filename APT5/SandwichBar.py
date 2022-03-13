"""
Created on 10/28/2021

@author: alyssa
"""
def canmake(preference, available):
    listOrders = preference.split()
    setOrders = set(listOrders)
    setAvailable = set(available)
    overlap = setOrders & setAvailable
    if len(overlap) == len(setOrders):
        return True
    return False

def whichOrder (available, orders):
    for dex in range(len(orders)):
        if canmake(orders[dex],available):
            return dex
    return -1

if __name__ == '__main__':
    print (whichOrder ([ "cheese", "cheese", "cheese", "tomato" ],[ "ham ham ham", "water", "pork", "bread", "cheese tomato cheese", "beef" ]))
