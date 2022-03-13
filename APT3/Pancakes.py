"""
Created on 10/4/2021

@author: alyss
"""

def minutesNeeded(numCakes, capacity):
    """
    return integer representing time to cook pancakes
    based on integer parameters as described below
    """

    full = numCakes // capacity
    left = numCakes % capacity
    minutes = 10 * full
    if left > capacity/2:
        minutes += 10
    elif left > 0:
        minutes += 5

    return minutes

if __name__ == '__main__':
    pass
