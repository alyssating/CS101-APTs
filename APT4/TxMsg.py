"""
Created on 10/12/2021

@author: alyssa
"""
"""
Spaces are maintained, and each word is encoded individually. 
A word is a consecutive string of alphabetic characters.
If the word is composed only of vowels, it is written exactly as 
in the original message.
If the word has at least one consonant, write only the consonants 
that do not have another consonant immediately before them. 
Do not write any vowels.
The letters considered vowels in these rules are 'a', 'e', 'i', 'o' and 'u'. 
All other letters are considered consonants
"""

def isAllVowels(word):
    """
    returns True if all characters in word are vowels
    """
    vowels = "aeiouAEIOU"
    for char in word:
        if char not in vowels:
            return False
    return True

def encode(word):
    if isAllVowels(word):
        return word
    else:
        vowels = "aeiouAEIOU"
        newWord = ""
        for i in range(len(word)):
            if (word[i] not in vowels) and (word[i-1] in vowels or i == 0):
                newWord += word[i]
        return newWord

def getMessage(original):
    """
    return String that is 'textized' version
    of String parameter original
    """

    ret = []
    for word in original.split():
        ret.append(encode(word))
    return " ".join(ret)

if __name__ == '__main__':
    pass
