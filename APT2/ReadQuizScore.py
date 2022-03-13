"""
Created on 9/26/2021

@author: alyssa
"""

def grade(total, availablePoints, cutOff):
    """
    return a student's reading quiz grade as a float percentage based on
    the integer values in total, availablePoints, and cutOff.
    """

    minimumScore = (cutOff/100) * availablePoints

    if total >= minimumScore:
        grade = 100.0
        return grade

    else:
        grade = (total / minimumScore) * 100
        return grade

if __name__ == '__main__':
    print (grade(81, 100,80))