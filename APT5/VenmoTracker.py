"""
Created on 10/27/2021

@author: alyssa
"""

def networth(transactions):
    venmo={}
    for entry in transactions:
        single=entry.split(":")
        sender=single[0]
        receiver=single[1]
        amount=int(float(single[2])*100)
        if sender not in venmo:
            venmo[sender]=0
        if receiver not in venmo:
            venmo[receiver] = 0
        venmo[sender]-=amount
        venmo[receiver]+=amount

    output=[]
    for name in sorted(venmo):
        output.append(name+":"+str(venmo[name]/100))
    return output


if __name__ == '__main__':
    pass
