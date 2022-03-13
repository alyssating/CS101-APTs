"""
Created on 10/9/2021

@author: alyssa ting
"""

def calculateBMI(input):
    '''
    The list parameter input contains two integers in the
    format [weight, height], where:

         weight-person's weight (in pounds (lbs)).

         height-person's height (in inches (in)).

    The function should return an integer that
    represents the calculated BMI.
    '''

    bmi = int((input[0]/input[1] ** 2) * 703)
    return bmi

# you write code here
if __name__ == '__main__':
    pass
