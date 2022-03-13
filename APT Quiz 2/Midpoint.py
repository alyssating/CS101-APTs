"""
Created on 11/13/2021

@author: alyssa ting
"""

def getPoint(coordinates):
    '''
    The function accepts one parameter named coordinates, which is a list
    containing two strings in the format ["x1,y1", "x2,y2"], where:

      "x1,y1" is an (x,y) coordinate pair for the first point

      "x2,y2" is an (x,y) coordinate pair for the second point

    The function should return a list containing the x and y coordinates of
    the midpoint in the format [x,y].
    ((x1+x2)/2, (y1+y2)/2) = midpoint
    '''
    x1 = int(coordinates[0].split(",")[0])
    x2 = int(coordinates[1].split(",")[0])
    y1 = int(coordinates[0].split(",")[1])
    y2 = int(coordinates[1].split(",")[1])
    return [(x1+x2)/2,(y1+y2)/2]

if __name__ == '__main__':
    print (getPoint(["2,2", "2,2"]))
