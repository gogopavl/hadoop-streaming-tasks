#!/usr/bin/env python2
# task2/mapper.py
import sys
from collections import defaultdict

bigramDictionary = defaultdict(int) # Structure to temporarily save bigram terms
MAX_SIZE = 500 # Variable to limit dictionary size - O(1) memory complexity

def getBigrams(inputList):
    """Given a list of terms forms all bigrams

    Parameters
    ----------
    inputList : List of Strings
        A list containing individual words

    Returns
    -------
    bigram list : List of Strings
        The list with the formed bigram pairs
    """
    return zip(inputList, inputList[1:]) # zip returns all tuple pairs from given inputs

def map_function(line):
    """Given a line emits (key, value) pairs, where key = bigram and value = 1 - the occurrence

    Parameters
    ----------
    line : String type
        A line from the input stream

    Returns
    -------
    bigram, 1 : Tuple
        The formed bigram and 1 - its occurrence
    """
    wordList = line.strip().split()
    bigramList = getBigrams(wordList)
    for bigram in bigramList:
        yield (bigram[0] + '_' + bigram[1]), 1 # Yield bigram with underscore and 1

for line in sys.stdin:
    for key, value in map_function(line):
        bigramDictionary[key] += value # Aggregate bigram occurrence

        if len(bigramDictionary) >= MAX_SIZE: # When structure reaches MAX_SIZE print and then clear it
            for key, value in bigramDictionary.iteritems():
                print(key + "\t" + str(value))
            bigramDictionary.clear()

for key, value in bigramDictionary.items(): # Emit leftover pairs
    print(key + "\t" + str(value))
