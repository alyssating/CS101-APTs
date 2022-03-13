"""
Created on 10/9/2021

@author: alyssa ting
"""


def expenses(spending, limit):
    '''
    This function accepts two parameters:
       spending-list parameter of 12 integers that represent
       the total expenses for each month of the year.

       limit-the maximum amount that can be spent for the year.

    The function should return a string representing the first
    month where the total expenses incurred for the year up to
    that month exceed the yearly limit.
    '''

    total = 0
    count = 0
    for value in spending:
        if total <= limit:
            total += value
            count += 1

    if count == 1:
        return "January"
    elif count == 2:
        return "February"
    elif count == 3:
        return "March"
    elif count == 4:
        return "April"
    elif count == 5:
        return "May"
    elif count == 6:
        return "June"
    elif count == 7:
        return "July"
    elif count == 8:
        return "August"
    elif count == 9:
        return "September"
    elif count == 10:
        return "October"
    elif count == 11:
        return "November"
    elif count == 12:
        return "December"

if __name__ == '__main__':
    pass