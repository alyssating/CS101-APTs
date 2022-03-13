"""
Created on 11/25/2021

@author: alyssa
"""


def getStats(sentence):
    '''
    sentence (str) - a string with a potential pangram in it

    For all the letters return a list where value at the kth index is the
    number of letters that occur k times.
    '''

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    dict = {}
    for i in list(alphabet):
        if i not in dict:
            dict[i] = 0
    for i in sentence.split():
        for x in list(i):
            if x.lower() in alphabet:
                dict[x.lower()] += 1
    sortedLst = sorted(dict.items(), key = lambda x: x[1])

    # making a dictionary with the number of letters that appear x times
    dictfreq = {}
    for x in sortedLst:
        if x[1] not in dictfreq:
            dictfreq[x[1]] = 0
        dictfreq[x[1]] += 1

    # adding 0s
    lst = list(dictfreq.items())
    for i in range(lst[-1][0]):
        if i not in dictfreq.keys():
            dictfreq[i] = 0

    ret = []
    for i in sorted(dictfreq.items()):
        ret.append(i[1])
    return ret

if __name__ == '__main__':
    print (getStats("This Pangram contains four a's, one b, two c's, one d, "
                    "thirty e's, six f's, five g's, seven h's, eleven i's, one j,"
                    "one k, two l's, two m's, eighteen n's, fifteen o's, two p's, "
                    "one q, five r's, twenty-seven s's, eighteen t's, two u's, "
                    "seven v's, eight w's, two x's, three y's, & one z."))
