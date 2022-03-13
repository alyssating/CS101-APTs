"""
Created on 10/8/2021

@author: alyssa
"""

def calculate(coef3, coef2, coef1, coef0, x):
    """
    coef3 is the coefficient for x^3
    coef2 is the coefficient for x^2
    coef1 is the coefficient for x^1
    coef0 is the coefficient for x^0

    Given the coefficients for a cubic equation,
    and a value x, calculate and return the value
    of the cubic equation for x.

    Calculate the answer as a float.
    """

    return (coef3 * (x ** 3)) + (coef2 * (x ** 2)) + (coef1 * x) + coef0

if __name__ == '__main__':
    pass
