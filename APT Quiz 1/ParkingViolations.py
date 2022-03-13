"""
Created on 10/9/2021

@author: alyssa ting
"""

import math
def amountOwed(ticket, months):
    '''
    The following parameters are input to the function:
      ticket-the original ticket amount.
      months-the number of months that the fine is late.


    The function should return the current amount owed, which includes
    the parking fee plus all late fees.
    '''

    total = ticket * (1.05 ** months)
    return math.ceil(total)

if __name__ == '__main__':
    pass
