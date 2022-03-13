"""
Created on 10/28/2021

@author: alyss
"""

def bags(strength,food):
    foodList = []
    count = 0
    for x in food:
        if x not in foodList:
            foodList.append(x)
            count += 1
        elif x in foodList:
            if foodList.count(x) % strength == 0:
                count += 1
                foodList.append(x)
            else:
                foodList.append(x)
    return count

if __name__ == '__main__':
    print (bags(2,["DAIRY","DAIRY","PRODUCE","PRODUCE","PRODUCE","MEAT"]))
