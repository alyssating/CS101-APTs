"""
Created on 12/10/2021

@author: alyssa ting
"""


def leader(info):
    '''
    The parameter info is a list of strings in the format

    "school:wins:losses"

    The function should return a list of the school(s) with the
    least losses.
    '''

    lst = [(i.split(":")[0],i.split(":")[-1]) for i in info]
    return [i[0] for i in lst if i[1] == sorted(lst,key = lambda x: x[1])[0][1]]

    # # less efficient solution
    # lst = [(i.split(":")[0],i.split(":")[-1]) for i in info]
    # ret = []
    #
    # for i in lst:
    #     if i[1] == sorted(lst, key = lambda x: x[1])[0][1]:
    #         ret.append(i[0])
    # return ret

if __name__ == '__main__':
    print (leader(["UNC:4:5", "Duke:8:1", "Wake Forest:7:2", "NCSU:8:1"]))
