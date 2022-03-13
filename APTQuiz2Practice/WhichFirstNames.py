"""
Created on 11/11/2021

@author: alyss
"""

def computeNames(team1, count, team2):
    '''
    You have three parameters, team1,
    count, and team2.
    The two string parameters are
    named team1 and team2, where both
    of them are a string of peoples names,
    with words separated by blanks.
    Each name on a team is exactly two words.
    The count parameter is an integer
    and indicates the number of teams. It
    will always have the value 2.
    This function returns a string of the
    unique first names that are only
    in one of the teams. The names should
    appear in alphabetical order.
    '''

    lst1 = []
    lst2 = []
    count = 0
    while count <= len (team1.split()) - 2:
        lst1.append(team1.split()[count])
        count += 2 #so that it only adds first names to the list
    count = 0
    while count <= len(team2.split()) - 2:
        lst2.append(team2.split()[count])
        count += 2

    return " ".join(sorted(list(set(lst1) ^ set(lst2))))
if __name__ == '__main__':
    print(computeNames("Joe Smith Wes Smith Joe Wright Craig Wills",2, "Bill Carter Wes Mitchell Craig Smith"))
