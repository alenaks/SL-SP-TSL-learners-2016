#!/usr/bin/python

""" Path is a [a, [b, c], d] list, where 'a' and 'd' is a subsequence
    of a string, 'a' precedes 'a', and [b, c] is the set of all
    elements that can be found between them, so the path above is one
    of the path in word "abccd", for example
"""


def find_paths(text):
    """ Returns list of paths of a given text
        Input: list of words
        Output: list of paths
    """
    
    paths = []
    for i in text:
        word_path = path(i)
        for j in word_path:
            if j not in paths:
                paths.append(j)
                
    return paths



def path(word):
    """ Returns list of paths of a given word
        Input: word
        Output: list of paths
    """
    
    word = "#" + word + "#"
    word_paths = []
    
    for i in range(len(word)-1):
        for j in range(i+1,len(word)):
            path = []
            
            inter = []
            for k in word[i+1:j]:
                if k not in inter:
                    inter.append(k)

            path.append(word[i])
            path.append(inter)
            path.append(word[j])

            if path not in word_paths:
                word_paths.append(path)

    return word_paths
