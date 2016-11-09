#!/usr/bin/python

# Jardine's example:
# tatalat, atattatalat, attatatalat, talarat, latarat, talatarat, tlaralat, tataltralat, lataralat, tatrat, tarta


""" This program is a 2TSL learner by Jardine (2016).
    The learner induces a tier and learns the grammar.
"""

from copy import deepcopy
from extract_paths import *
from get_tier import *
from SLmain import *



def TSLmain():
    """ Autorunned complete version of TSL learner

        Input: autorun, asks for list of words
        Output: None; prints alphabet and grammar 
    """
    
    text = input("Input list:\n").split(", ")
    TSLgrammar = findTSL(text)

    print("\nTier alphabet:\n", TSLgrammar[0])
    print("\nList of tier bigrams:\n", TSLgrammar[1])
        


def findTSL(text):
    """ Returns TSL grammar based on the fiven text

        Input: list of words
        Output: grammar = [tier, tier_bigrams]
    """
    alphabet = alphabetize(text)
    sigma = deepcopy(alphabet)
    
    paths = find_paths(text)
    result = get_tier(sigma, alphabet, paths)
    tier, PT = result[0], result[1]

    nontier = set(sigma).difference(set(tier))           
    tier_copy = deepcopy(tier) + ["#"]
    
    tier_bigr = []
    for i in PT:
        if (i[0] in tier_copy) and (i[2] in tier_copy) and \
           (set(i[1]).issubset(nontier)):
            bigram = i[0]+i[2]
            if bigram not in tier_bigr:
                tier_bigr.append(bigram)

    grammar = [sorted(tier), sorted(tier_bigr)]

    return grammar
