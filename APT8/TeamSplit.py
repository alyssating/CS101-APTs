"""
Created on 11/25/2021

@author: alyssa
"""


def difference(strengths):
    """
    return int based on int list parameter strengths
    """

    team1 = []
    team2 = []
    while len(strengths) > 0:
        team1.append(max(strengths))
        strengths.remove(max(strengths))
        if len(strengths) > 0:
            team2.append(max(strengths))
            strengths.remove(max(strengths))
    return (abs(sum(team1)-sum(team2)))

if __name__ == '__main__':
    print(difference([824, 581, 9, 776, 149, 493, 531, 558, 995, 637,
 394, 526, 986, 548, 344, 509, 319,  37, 790, 491,
 479,  34, 776, 321, 258, 851, 711, 365, 763, 355,
 386, 877, 596,  96, 151, 166, 558, 109, 874, 959,
 845, 181, 976, 335, 930,  22,  78, 120, 907, 584]))
