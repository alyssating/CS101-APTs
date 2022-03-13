"""
Created on 11/4/2021

@author: alyss
"""


def winners(ballot):
    """
    return list of winners based on votes
    in list ballot
    """

# adding all candidates to the dictionary
    dict = {}
    for elm in ballot:
        lst = elm.split()
        for i in range(len(lst)):
            dict[lst[i]] = 0

# adding up the points for each candidate based on their position in the list
    for elm in ballot:
        lst2 = elm.split()
        for i in range(len(lst2)):
            dict[lst2[i]] += len(lst2) - i
    lstVotes = sorted(dict.items(), key = lambda x: -x[-1])

# adding the winners to the return list, also checking if there is more than one winner
    ret = []
    for elm in lstVotes:
            ret.append(elm[0])
    return sorted(ret)

if __name__ == '__main__':
    print (winners(['slim jim tim kim', 'jim slim tim kim', 'jim slim tom tam', 'slim jim tom tam', 'tom tam bob jim', 'tom tam bob slim', 'tam tom bob jim', 'tam tom bob slim']))
