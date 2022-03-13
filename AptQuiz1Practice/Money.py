"""
Created on 10/8/2021

@author: alyssa
"""

def toMillion(principal, contribution, interest):
    """
    principal (int) -  account starting value
    contribution (int) - yearly contribution
    interest (float) - yearly compounded interest

    Return the number of years it would take for an account to reach a million
    dollars, where the account starts at PRINCIPAL, is compounded yearly at
    INTEREST, and CONTRIBUTION is added to the account at the beginning of
    every year.
    """

    total = (principal + contribution) * (1 + interest)
    count = 0
    if principal >= 1000000:
        return 0
    else:
        while total < 1000000:
            total = (total + contribution) * (1 + interest)
            count += 1
        return count + 1

if __name__ == '__main__':
    principal = 863837
    contribution = 1
    interest = 0.05

    print (toMillion(principal, contribution, interest))
