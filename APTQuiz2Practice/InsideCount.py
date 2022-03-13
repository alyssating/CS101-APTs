"""
Created on 11/11/2021

@author: alyssa
"""

def howMany(phrase, letter):
    '''
    Given string parameters phrase and letter,
    where letter is one character and phrase is a
    string of words separated by a blank, return
    the count of the unique words in phrase
    that have letter in them
    '''
    lst = []
    for word in phrase.split():
        if word.lower() not in lst:
            lst.append(word.lower())
    count = 0
    for item in lst:
        if letter in item:
            count += 1
    return count

if __name__ == '__main__':
    print (howMany("Duke CompSci graduates are Jedi Masters of the technology sector","d"))
