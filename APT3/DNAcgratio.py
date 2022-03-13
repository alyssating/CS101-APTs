"""
Created on 9/30/2021

@author: alyssa
"""

def ratio(dna):
    """
    return float that's the cg ratio of the
    nucleotides in the string parameter dna

    Given a strand of DNA determine the percentage of cytosine and guanine
    nucleotides present in the genome. Your method should return the percentage
    (between 0.0 and 1.0) of 'c' (cytosine) and 'g' (guanine) in the genome.
    For example, if half of the nucleotides are either 'c' or 'g' your method
    should return 0.5 --- see the examples for more detail
    """

    numC = dna.count("c")
    numG = dna.count("g")
    numTotal = len(dna)

    percent = (numC+numG)/numTotal
    return percent

if __name__ == '__main__':
    print(ratio("agatc"))
