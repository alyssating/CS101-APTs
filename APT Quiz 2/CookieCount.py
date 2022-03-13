"""
Created on 11/13/2021

@author: alyssa ting
"""

def countOrders(orders):
    '''
    The list parameter orders contains a string in the format
    "name:order:quant:name:order:quant:name:order:quant:name:order:quant",
    where:

         name-first name of a person.

         order-the type of cookie ordered.

         quant-the number of boxes requested.

    The function should return an integer that represents the maximum number of
    boxes ordered of any type of cookie.
    '''

    splits = orders.split(":")
    dex = 0
    splitOrders = []
    while dex <= 9:
        splitOrders.append(splits[dex:dex+3])
        dex += 3

    dict = {}
    for order in splitOrders:
        if order[1] not in dict:
            dict[order[1]] = int(order[-1])
        else:
            dict[order[1]] += int(order[-1])
    return sorted((dict.items()), key = lambda x: x[1], reverse = True)[0][1]

if __name__ == '__main__':
    print (countOrders("Kim:Samoas:6:Kim:Adventurefuls:2:Kim:Lemonades:4:Kim:Tagalongs:10"))
