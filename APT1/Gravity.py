"""
Created on 9/3/2021

@author: alyssa
"""

def falling(time,velo):
    g = 9.8
    d = velo*time + 0.5*g*time**2
    print (time)
    return d

if __name__ == '__main__':
    x = falling (3,4)
    print (x)