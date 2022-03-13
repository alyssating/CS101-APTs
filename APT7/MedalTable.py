"""
Created on 11/17/2021

@author: alyssa
"""

def generate(results):
    """
    return list of strings
    based on data in results, a list of strings
    """
    # {USA: [1,1,1]}

    dict = {}
    for i in results:
        for x in i.split():
            if x not in dict:
                dict[x] = [0,0,0]

    for i in results:
        dict[i.split()[0]][0] += 1
        dict[i.split()[1]][1] += 1
        dict[i.split()[2]][2] += 1

    sortedLst = sorted(sorted(sorted(sorted(dict.items()), key=lambda x: -x[1][-1]),
                  key=lambda x: -x[1][1]), key=lambda x: -x[1][0])

    ret = []
    for i in sortedLst:
        ret.append(i[0] + " " +" ".join([str(x) for x in i[1]]))

    return ret

if __name__ == '__main__':
    print (generate(["ITA JPN AUS", "KOR TPE UKR", "KOR KOR GBR", "KOR CHN TPE"]))
