#!/usr/bin/python

""" This program helps you to find SP patterns
    in the inputted language.
"""

from SLmain import *

def SPmain():
    """ Autorunned complete version of SP learner

        Input: autorun, asks for list of words
        Output: None; prints alphabet and grammar 
    """
    
    text = input("Please, enter words here:\n").split(", ")

    sigma = alphabetize(text)
    SPgrammar = findSP(text)

    print("\nAlphabet:\n", sigma)
    print("\nSP grammar:\n", SPgrammar)



def findSP(text):
    """ Returns list of subsequences of the text

        Input: list of words
        Output: list of subsequences
    """
    
    SPgrammar = []
    
    for i in text:
        for j in SPword(i):
            if j not in SPgrammar:
                SPgrammar.append(j)

    return SPgrammar



def SPword(word):
    """ Returns list of subsequences of the word

        Input: word
        Output: list of subsequences
    """
    
    word = "#" + word + "#"

    SPword = []
    for i in word:
        for j in word[word.index(i)+1:]:
            bigram = i+j
            if bigram not in SPword:
                SPword.append(i+j)
    
    return SPword
