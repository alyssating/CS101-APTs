"""
Created on 12/10/2021

@author: alyssa ting
"""


def zipTracker(zips):
    '''
    The list parameter zips contains a string of five-digit zip codes

    The function should return an integer that represents the number
    of Durham zip codes in the list.
    '''

    return sum([1 for zip in zips if zip[:3] == "277"])

    # # less efficient solution:
    # count = 0
    # for zip in zips:
    #     if zip[:3] == "277":
    #         count += 1
    # return count

if __name__ == '__main__':
    zips = ['27707', '28216', '27517', '28273']
    print (zipTracker(zips))
