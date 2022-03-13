"""
Created on 12/10/2021

@author: alyssa
"""


def nickname(year):
    '''
    year (int) - A year between 1950 and 2019 inclusively

    Return a string with the nickname of the year in the parameter.
    '''

    if year <= 1959 and year >= 1950:
        return "50s"
    elif year <= 1969 and year >= 1960:
        return "60s"
    elif year <= 1979 and year >= 1970:
        return "70s"
    elif year <= 1989 and year >= 1980:
        return "80s"
    elif year <= 1999 and year >= 1990:
        return "90s"
    elif year <= 2009 and year >= 2000:
        return "aughts"
    elif year <= 2019 and year >= 2010:
        return "twenty-tens"

if __name__ == '__main__':
    pass
