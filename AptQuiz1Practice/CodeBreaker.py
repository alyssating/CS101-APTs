"""
Created on 10/7/2021

@author: alyssa
"""
def compute(phrase, one, two, sep):
    '''
    Given the four string parameters
    phrase, one, two and sep,
    return a string of the decoded
    message.
    CONDITIONS:
    1) If the word starts with one then the last letter of the word is part of
    the message.
    2) If the word contains two as part of it, then the third letter of the word
    is part of the message, if the third letter exists.
    3) If the word starts or ends with sep, then a dash, '-', is part of the
    message.
    If more than one of 1), 2) or 3) match, use the first such one that matches.
    '''

    list = phrase.split()
    decoded = ""

    for i in list:
        if i[0] == one:
            decoded += i[-1]
        elif (two in i) and (len(i)>=3):
            decoded += i[2]
        elif i[0] == sep or i[-1] == sep:
            decoded += "-"
    return decoded

if __name__ == '__main__':
    print(compute("this is a long story left","l","i","s"))