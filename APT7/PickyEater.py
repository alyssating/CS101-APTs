"""
Created on 11/17/2021

@author: alyssa
"""

def dinner(foods, willEat, hunger, meal):
    '''
    foods (list of strings) - parallel list with willEat of the foods picky
        eater is willing to eat.
    willEat (list of ints) - parallel list with foods of how much of that food
        the picky eater is willing to eat.
    hunger (int) - how much food the picky eater needs to eat to be full.
    meal (list of strings) - the list and order of the foods given to the picky
        eater.

    Return how much food the picky eater still needs to eat to be full.
    '''

    dict = {}
    for i in range(len(foods)):
        if foods[i] not in dict:
            dict[foods[i]] = willEat[i]

    hunger = hunger
    length = len(meal)
    for food in meal:
        if dict[food] > 0:
            hunger -= 1
            dict[food] -= 1
        length -= 1

    if hunger <= 0:
        return 0
    return hunger

if __name__ == '__main__':
    print (dinner(['ice cream', 'chocolate', 'broccoli'], [100, 10, 0],3,['broccoli', 'ice cream', 'ice cream', 'chocolate', 'ice cream']))
