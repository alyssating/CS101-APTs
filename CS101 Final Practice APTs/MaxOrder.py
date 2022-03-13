"""
Created on 12/10/2021

@author: alyssa
"""

def forItem(orders, item):
    '''
    orders (list of strs) - list of orders for items in format "ITEM:QUANTITY"
    item (str) - item of interest in ORDERS

    Return in a list the largest ordered quantity for ITEM in ORDERS
    and how many times that quantity was ordered.
    '''

    lst = [(i.split(":")[0],int(i.split(":")[1])) for i in orders]

    if item not in [x[0] for x in lst]:
        return [0,0]

    maxCount = 0
    count = 0

    for i in lst:
        if i[0] == item and i[1] >= maxCount:
            maxCount = i[1]

    for i in lst:
        if i[0] == item and i[1] == maxCount:
            count += 1

    return [maxCount,count]

if __name__ == '__main__':

    orders = ['banana:4', 'orange:22', 'banana:4', 'banana:3']
    item = 'banana'
    print (forItem(orders,item))
