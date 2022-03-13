"""
Created on 11/11/2021

@author: alyssa
"""


def selectCities(locations1, locations2, locations3):
    '''
    locations1 (list of strings) - friend #1's preferred cities
    locations2 (list of strings) - friend #2's preferred cities
    locations3 (list of strings) - your preferred cities

    '''

    inAll = set(locations1) & set(locations2) & set(locations3)

    setPossible = (set(locations1) | set(locations2) | set(locations3)) - inAll
    return len(setPossible)

if __name__ == '__main__':
    print (selectCities(["Miami", "DC"],["Vegas", "Miami"],["Chicago", "Miami"]))
