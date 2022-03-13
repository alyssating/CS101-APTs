"""
Created on 9/26/2021

@author: alyssa
"""

def combine(first, flen, second, slen):
    """
    return string that's a portmanteau
    of strings first and second
    using flen chars from first
    and slen chars from second
    """

    firstPart = first[:flen]
    secondPart = second[-slen:]

    return firstPart + secondPart

if __name__ == '__main__':
    pass