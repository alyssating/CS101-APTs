"""
Created on 11/17/2021

@author: alyssa
"""

def nameDonor(contributions):
    """
    The parameter contributions is a list of strings,
    return stringthat is name of most
    generous donor. See description for details.
    """
    dict = {}
    for donor in contributions:
        if donor.split(":")[0] not in dict:
            dict[donor.split(":")[0]] = 0.0
        dict[donor.split(":")[0]] += float(donor.split(":")[1])
    return sorted(sorted(dict.items()), key = lambda x: x[1], reverse = True)[0][0]

# ["Sun:70.00", "Zebra:80.00", "Blue:80.00", "Edwards:50.00"]
if __name__ == '__main__':
    print (nameDonor(["Sun:70.00", "Zebra:80.00", "Blue:80.00", "Edwards:50.00"]))
