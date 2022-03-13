"""
Created on 9/6/2021

@author: alyssa
"""

def minutesNeeded(m):
    time=25*(m+1)+10
    return time

    """
    Return integer number of minutes to launder m (integer) loads
    Washing a load takes 25 minutes, drying a load takes 25 minutes, and folding the clothes in a load takes 10 minutes,
    for a total of 1 hour per load (assuming that the time to transfer a load is built into the timings given). 10 loads
    of laundry can be done in 10 hours, 600 minutes, using the method of completing one load before starting the next one.
    Though it can be done faster, see examples. Write the method, minutesNeeded, that returns the shortest time needed to
    do m loads of laundry. In other words, given an integer value representing the number of loads to complete, m,
    determine the smallest number of minutes needed to complete all loads of laundry.
    """

if __name__ == '__main__':
    pass