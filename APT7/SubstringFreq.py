"""
Created on 11/17/2021

@author: alyssa
"""


def frequency(text, n):
    '''
    text (string) - A string with at least one word
    n (int) - the length of the substring

    Counts the appearance of each substring in text and returns the most frequent ones as a list.
    '''

    dict = {}
    for word in text.split():
        length = len(word)
        for i in range(length - (n-1)):
            substring = word[i:i+n]
            if substring not in dict:
                dict[substring] = 0
            dict[substring] += 1
    maxFreq = max([i[1] for i in dict.items()])
    ret = []
    for tpl in dict.items():
        if tpl[1] == maxFreq:
            ret.append(tpl[0])
    return sorted(ret)

if __name__ == '__main__':
    print (frequency('itkfkf fkf jtfjgf kh dhfdch',1))
