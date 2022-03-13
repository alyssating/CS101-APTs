"""
Created on 9/6/2021

@author: alyssa
"""

def volume(radius, height):
    x=(1/3)*3.1415926*radius**2*height
    return x
    """
    return volume of a cone in cubic inches
    given float parameters radius and height in inches
    volume formula: 1/3 * pi * r**2 * h
    """

if __name__ == '__main__':
    print (volume(1,2))
