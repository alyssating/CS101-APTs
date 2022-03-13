"""
Created on 12/10/2021

@author: alyssa ting
"""

def arrears(transactions):
    '''
    The function accepts one parameter named transactions,
    which is a list of strings in the format

      "accountType:action:amount", where:

      "accountType" - "checking" or "savings"

      "action" - "deposit" or "withdraw"

      "amount" - numeric amount to deposit/withdraw

    The function should return an integer representing the number of accounts with a negative balance.
    '''

    dict = {"checking":0,"savings":0}
    for i in transactions:
        if i.split(":")[1] == "deposit":
            dict[i.split(":")[0]] += int(i.split(":")[-1])
        elif i.split(":")[1] == "withdraw":
            dict[i.split(":")[0]] -= int(i.split(":")[-1])
    count = 0
    for i in dict.items():
        if i[1] < 0:
            count += 1
    return count

if __name__ == '__main__':
    print (arrears(["checking:deposit:20", "savings:deposit:20", "checking:withdraw:20"]))
