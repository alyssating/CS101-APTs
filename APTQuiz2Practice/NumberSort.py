"""
Created on 11/11/2021

@author: alyss
"""


def sortnumbers(values):
    '''
    The list parameter <i>values</i> contains a list of integers .

   The function should add 1 to each item in the list, and return the new list in descending order.
    '''

    return sorted([v + 1 for v in values], reverse = True)
if __name__ == '__main__':
    pass
