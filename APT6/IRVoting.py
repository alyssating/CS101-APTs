"""
Created on 11/4/2021

@author: alyssa
"""


def winner3(data):
    '''
    data (list of strs): A list of strings, each string represents a voter's
        ranked preference for the three candidates. Each candidate is separated
        by a semicolon ";"

    Implement instant runoff voting when there are only three candidates to
    choose from. Return the candidate that wins or 'Tie' if there is a tie.
    '''

    dict = {}
    for elm in data:
        if elm.split(";")[0] not in dict.keys():
            dict[elm.split(";")[0]] = 1
        else:
            dict[elm.split(";")[0]] += 1
    lst = list(dict.items())
    sortedLst = sorted(lst, key = lambda x: -x[1])
    if sortedLst[0][1] > len(data) / 2:
        return sortedLst[0][0]
    else:
        loser = sortedLst[-1][0] # determining whose votes to redistribute
        for elm in data:
            voters = elm.split(";")
            if voters[0] == loser: # finding who put the loser as their first choice
                dict[voters[1]] += 1 # giving the vote to the voter's second choice
        lst2 = list(dict.items())
        sortedLst2 = sorted(lst2, key = lambda x: -x[1])
        if sortedLst2[0][1] == sortedLst2[1][1]: # checking for a tie
            return "Tie"
        else:
            return sortedLst2[0][0]

if __name__ == '__main__':
    print (winner3(['Jackqueline;Mckenzie;Angelena', 'Jackqueline;Mckenzie;Angelena', 'Jackqueline;Angelena;Mckenzie',
        'Mckenzie;Jackqueline;Angelena',
        'Angelena;Jackqueline;Mckenzie']))