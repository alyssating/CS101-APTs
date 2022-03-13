"""
Created on 10/15/2021

@author: alyssa
"""


def findChildren(parents,children,person):
    parentdex = []
    dex = 0
    for parent in parents:
        dex += 1
        if parent == person:
            parentdex.append(dex-1)
    parentsChildren = []
    for dex in parentdex:
        parentsChildren.append(children[dex])

    return parentsChildren


def grandchildren(parents, children, person):
    '''
    parents (list of strings) - list of parent names corresponding to the
        children list
    children (list of strings) - list of child names corresponding to the
        parents list
    person (string) - a person listed in parents

    Return the number of grandchildren for the person in the person variable
    '''

    ret = 0
    childrenList = findChildren(parents,children,person)
    for child in childrenList:
        grandchildrenList = findChildren(parents,children,child)
        ret += len(grandchildrenList)
    return ret

if __name__ == '__main__':
    print (grandchildren(['Junhua', 'Anshul', 'Junhua', 'Anshul', 'Kerry'],['Anshul', 'Jordan', 'Kerry', 'Paul', 'Kai'],'Junhua'))