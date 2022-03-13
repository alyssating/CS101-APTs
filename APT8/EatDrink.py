"""
Created on 11/22/2021

@author: alyssa
"""


def winners(data):
    """
    return String list based on String list data
    """

    dict = {}
    for x in data:
        if x.split()[0] not in dict:
            dict[x.split()[0]] = [0,0]
        dict[x.split()[0]][0] += 1
        seconds = int(x.split()[-1].split(":")[-1]) + int(x.split()[-1].split(":")[0])*60
        dict[x.split()[0]][1] += seconds

    print (dict.items())

    return [i[0] for i in sorted(sorted(dict.items(), key = lambda x: x[1][1]), key = lambda x: x[1][0], reverse = True)]

if __name__ == '__main__':
    print (winners(["tyson 0:11", "usain 0:12", "carl 0:30", "carl 0:20", "usain 0:40",
            "carl 1:00", "usain 0:57"]))
