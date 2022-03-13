"""
Created on 11/13/2021

@author: alyssa
"""

def bestBaker(scores):
    """
    scores (list of str) - list of strings in format "name:x:y"
                           judge's scores for contestants

    Return the winner of the baking contest.
    In other words the combined score is total_taste*0.6 + total_aesthetic*0.4.

    """
    dict = {}
    for score in scores:
        contestant = score.split(":")[0]
        combinedScore = int(score.split(":")[1])*0.6 + int(score.split(":")[2])*0.4
        if contestant not in dict:
            dict[contestant] = combinedScore
        else:
            dict[contestant] += combinedScore

    dict2 = {}
    for score in scores:
        contestant = score.split(":")[0]
        tasteScore = int(score.split(":")[1])
        if contestant not in dict2:
            dict2[contestant] = tasteScore
        else:
            dict2[contestant] += tasteScore
    ret = []
    for i in dict.items():
        ret.append((i[0],i[1],dict2[i[0]]))

    return sorted(sorted(ret, key = lambda x: x[-1], reverse = True), key = lambda x: x[1], reverse = True)[0][0]

if __name__ == '__main__':
    print (bestBaker([
    'Brian:3:3',
    'Brennan:3:2',
    'Brennan:2:2',
    'Brian:3:3',
    'Brennan:5:1',
    'Brian:2:2']))
