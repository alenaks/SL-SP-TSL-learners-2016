#!/usr/bin/python

""" This module extractis tiers.
    This version of the algorithm is Jardine (2016).

    get_tier(tier, paths) induces the tier.
    tier = set of elements on the tier, subset of the alphabet
    paths = possible paths for this tier symbols
"""

from extract_paths import *
from SLmain import *
from copy import deepcopy

def get_tier(sigma, tier, paths):
    """ Extracts the tier

        Input: alphabet, current tier alphabet, set of relevant paths
        Output: tier, list of tier paths
    """

    tier_copy = deepcopy(tier) + ["#"]
    nontier = set(sigma).difference(set(tier))
    nontier = list(nontier)

    for i in tier:
        change_ind = 0
        
        for j in tier_copy:
            for k in paths:
                if k[0] == i and k[2] == j and \
                   set(k[1]).issubset(set(nontier)):
                    for l in paths:
                        if l[0] == j and l[2] == i and \
                           set(l[1]).issubset(set(nontier)):
                            change_ind = change_ind + 1
                            break
                    break

        if change_ind == len(tier) + 1:
            tier.remove(i)
            nontier.append(i)
            tier_copy = deepcopy(tier) + ["#"]

            tier_paths = []
            for i in paths:
                if (i[0] in tier_copy) and (i[2] in tier_copy):
                    tier_paths.append(i)
            return get_tier(sigma, tier, tier_paths)
    
    return tier, paths
