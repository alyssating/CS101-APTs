"""
Created on 11/13/2021

@author: alyssa
"""

def winner(ballots):
    '''
    ballots (list of str) - Each string in this list is a voter's ballot

    Return the winner of the election based on highest score.
    '''
    dict = {}
    for i in ballots:
        for x in i.split():
            candidate = x.split(":")[0]
            vote = x.split(":")[1]
            if vote == "for":
                voteVal = 1
            if vote == "against":
                voteVal = -1
            if candidate not in dict:
                dict[candidate] = voteVal
            else:
                dict[candidate] += voteVal
    return sorted((dict.items()), key = lambda x: x[1], reverse = True)[0][0]

# ballots = ['Evan:for Madena:for','Evan:for Madena:for','Evan:for Bruny:for']
if __name__ == '__main__':
    print (winner(['Kristin:against Ceci:against', 'Kristin:against Ceci:against', 'Elisabeth:for', 'Elisabeth:against Kristin:against', 'Elisabeth:against Kristin:against']))
