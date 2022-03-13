"""
Created on 9/6/2021

@author: alyssa
"""

def convert(r, g, b):
    grayscale=0.21*r+0.716*g+0.07*b
    return float(grayscale)

    """
    return float value obtained by
    converting integer r,g,b, into grayscale
    
     Given integer Red/Green/Blue values, so-called (r,g,b) values, return the grayscale value given by the formula:
    0.21R + 0.71G + 0.07B
    """

if __name__ == '__main__':
    pass
