"""
Created on 10/4/2021

@author: alyss
"""


def modify(name):
    """
    name is a string with zero or more spaces
    with one space between each "word"
    return string "last, first MI. MI. MI. ..."
    where MI is middle initial
    """
    list = name.split()
    middleNames = list[1:-1]
    if len(list) == 1:
        newname = list[0]
    else:
        initials = ""
        for i in middleNames:
            if len(i) == 1:
                initials += " " + i[0]
            else:
                initials += " " + i[0] + "."

        newname = list[-1] + ", " + list[0] + initials
    return newname

if __name__ == '__main__':
    print (modify("Barrack"))
