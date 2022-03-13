"""
Created on 10/7/2021

@author: alyssa
"""


def toTen(lstOp, lstNum):
    '''
    lstOp (list of strings) - list of strings representing the
        operators +, -, *, /
    lstNum (list of ints) - list of integers

    Return the number of operations it takes to reach 10. If 10 is never
    reached, return -1. Starting at the beginning of the lists and with the
    value 0, add ('+'), subtract ('-'), multiply ('*'), or divide ('/') the
    current value with the current element in LST_NUM according to the current
    element in LST_OP.

    Implement the function toTen that takes two lists: lstOp and lstNum. lstOp
    is a list of math operators as strings: '+' (add), '-' (subtract), '*'
    (multiply), or '/' (divide). lstNum is a list of integers. The ith operator
    in lstOp should be used with the ith number in lstNum. Starting with the
    number 0, return the number of operations it takes to reach the value 10.
    If the code runs out of operators or numbers without reaching 10, return -1.
    '''
    position = 0
    total = 0
    while total != 10:
        if (position + 1) <= len(lstOp) and ((position + 1) <= (len(lstNum))):
            if lstOp[position] == "+":
                total = total + int(lstNum[position])
                position += 1
            elif lstOp[position] == "-":
                total = total - lstNum[position]
                position += 1
            elif lstOp[position] == "*":
                total = total * lstNum[position]
                position += 1
            elif lstOp[position] == "/":
                total = total / lstNum[position]
                position += 1
        else:
            if total != 10:
                return -1
            else:
                return position
    return position

if __name__ == '__main__':
    pass
