"""
Created on 10/27/2021

@author: alyssa
"""

def howMany (meals, restaurant):
    names = []
    for x in meals:
        data = x.split(":")
        name = data[0]
        place = data[1]
        if place == restaurant and name not in names:
            names.append(name)
    return len(names)

if __name__ == '__main__':
    pass
