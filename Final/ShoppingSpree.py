"""
Created on 12/10/2021

@author: alyssa ting
"""

def spending(cash):
    '''
    This function accepts one parameter, cash, which is an integer.

    The function should return a list of the number of candy, juice,
    salad, and pizza ordered (in this order).
    '''

    cash = cash
    lst = [4,2,12,10]
    ret = [0,0,0,0]
    while cash > 0:
        x = cash % 4
        cash -= lst[x]
        if cash >= 0:
            ret[x] += 1
    return ret

if __name__ == '__main__':
    print (spending(15))
