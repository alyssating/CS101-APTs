"""
Created on 11/11/2021

@author: alyssa
"""
def pickBest(groceries):
    '''
    Given the string parameter groceries,
    which contains items and for each
    item its cost from a particular store,
    return the total of the cheapest of
    each item.
    '''
    dict = {}
    for item in groceries.split(","):
        product = item.split(":")[0]
        price = float(item.split(":")[1])
        if product not in dict:
            dict[product] = 10000
        if price < dict[product]:
            dict[product] = price
    count = 0.0
    for i in dict.items():
        count += i[1]

    return count

if __name__ == '__main__':
    print (pickBest("peas:3.5,lotion:6.2,peas:3.5,peas:3.1,lotion:6.7"))
