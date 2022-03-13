"""
Created on 10/8/2021

@author: alyss
"""
def computeCups(calplan, eaten, calperserv, servsize):
    '''
    Here are the parameters for the function computeCups.
    calplan is an integer representing the number of
       calories you want to eat each day.
    eaten is an integer representing the number of
       calories you have eaten so far for a day
    calperserv is an integer representing the number of
       calories per serving for the cereal you would like
       to eat at the end of the day
    servsize is a float and represents the serving size
       in cups for this cereal
    Given these four parameters, return the number of full cups
       of cereal you could eat for a snack so that you won't go over
       the number of calories you want to eat each day.
    '''

    if eaten > calplan:
        return 0
    else:
        calLeft = calplan - eaten
        servingsLeft = calLeft / calperserv
        cups = servingsLeft * servsize
        return int(cups)

if __name__ == '__main__':
    print (computeCups(2000,1600,110,0.75))
