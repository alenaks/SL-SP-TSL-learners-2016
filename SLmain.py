#!/usr/bin/python


def SLmain():
    """ Autorunned complete version of SL learner

        Input: autorun, asks for list of words
        Example: ab, abab, ababab
        Output: None; prints alphabet and grammar 
    """
    
    text = input("Please, enter words here:\n")
    text = text.split(", ")

    sigma = alphabetize(text)
    SLgrammar = bigramize_text(text)

    print("\nAlphabet:\n", sigma)
    print("\nSL grammar:\n", SLgrammar)



def bigramize_text(text):
    """ For a given text, returns the list of bigrams

        Input: list of words
        Output: list of bigrams
    """
    
    bigrams = []
    for i in text:
        word_bigrams = bigramize_word(i)
        for j in word_bigrams:
            if j not in bigrams:
                bigrams.append(j)
    
    return bigrams



def bigramize_word(word):
    """ Creates list of bigrams based on the given word
        Input: word
        Output: list of bigrams
    """
    
    word = "#" + word + "#"
    bigrams = []
    for i in range(len(word)-1):
        bigram = word[i:i+2]
        if bigram not in bigrams:
            bigrams.append(bigram)
    return bigrams



def alphabetize(text):
    """ For a given text, collects its alphabet

        Input: list of words
        Output: sorted alphabet
    """
    
    alphabet = []
    for i in text:
        for j in i:
            if j not in alphabet:
                alphabet.append(j)
                
    return sorted(alphabet)
    
