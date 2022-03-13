"""
Created on 10/8/2021

@author: alyssa
"""

def transform(library,w):
    ret = ""
    dex = 0
    for i in library:
        dex += 1
        if i == w:
            ret+= w[dex]
    return ret

def decrypt(library, message):
    """
    return String for parameters
    library a list of Strings
    and message a string
    """

    ret = ""
    i = 0
    while i < len(message):
        char = transform(library,message)
        ret = ret + char
        i += 1
    return ret

if __name__ == '__main__':
    print (transform(["O ---", "S ..."],"... --- ..."))
