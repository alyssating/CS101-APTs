"""
Created on 10/12/2021

@author: alyssa
"""

def lovely(ingredients, inedible):
    """
    return int, number of items in
    ingredients, a string that are edible
    using informaion from  inedible, a string
    """

    ret = []
    for elm in ingredients.split():
        if elm not in inedible.split():
            ret.append(elm)
    return len(ret)

if __name__ == '__main__':
    print (lovely("a e i o u","b c d f g h j k l m n p q r s t v w x y z"))
