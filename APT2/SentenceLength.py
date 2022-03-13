"""
Created on 9/27/2021

@author: alyssa
"""

def average(sentenceList):
    """
    returns the average sentence length
    of all the sentences in sentenceList, a
    list of white-space delimited strings.
    """
    length = 0
    for element in sentenceList:
        List = element.split()
        length = length + len(List)

    return (length/len(sentenceList))

if __name__ == '__main__':
    pass