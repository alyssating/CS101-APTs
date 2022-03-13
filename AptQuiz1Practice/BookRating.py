"""
Created on 10/7/2021

@author: alyssa
"""
import math
def calculate(readpages, totalpages, numdays, amazon):
    """
    readpages - number of pages read
    totalpages - number of pages in the book
    numdays - number of days read book
    amazon - book rating on amazon

    Return the result of the formula shown.
    Calculate the answer as a float, then 
    return it as a truncated int
    """

    rating = int(math.sqrt((((readpages/totalpages)*1000)/numdays)**2+(amazon)**2))
    return rating

if __name__ == '__main__':
    print(calculate(356,356,10,4.12))
