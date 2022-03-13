"""
Created on 11/25/2021

@author: alyssa
"""

def maximumFacts(suspects):
    """
    return int based on information in
    parameter results, a list of strings
    """

    ret = []
    for i in range(len(suspects)):
        for x in range(len(suspects)):
            if i != x:
                overlap = len(set(suspects[i].split(",")) & set(suspects[x].split(",")))
                ret.append(overlap)
    if len(ret) > 0:
        return max(ret)
    return 0

if __name__ == '__main__':
    print (maximumFacts(["big,tall,loud,happy,male,scarred,tattooed,dirty",
                         "short,male,beard,quiet,happy,tanned,handsome",
                         "female,pretty,blond,quiet", "somnambulistic",
                         "happy,tiny,stout,male,tanned,beard,blond"]))