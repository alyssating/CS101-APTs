"""
Created on 11/17/2021

@author: alyssa
"""


def decrypt(message, numbers):
    '''
    message (string) - regular message with 1 or more words
    numbers (list of ints) - list of positive and negative integers

    Return the secret message hidden in message using the list numbers.
    '''
    string = ""
    for x in range(len(numbers)):
        if numbers[x] <= (len(message.split()[x])-1) and numbers[x] >= (-1*len(message.split()[x])):
            string += message.split()[x][numbers[x]]
    return string

if __name__ == '__main__':
    print (decrypt('Hello, it looks as if the bear symbol is all over campus. Why do they like the bear symbol, George?', [0, 0, 10, -4, 4, 0, 3, 4, 5, -4, -10, 4, 5, -6, -7, 6, 4, 0, 5, 1]))
