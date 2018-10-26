#!/usr/bin/env python2
# mapper2.py
import sys

from collections import defaultdict

bigramDictionary = defaultdict(int) # Structure to temporarily save bigram terms
MAX_SIZE = 500

def getBigrams(inputList):
    return zip(inputList, inputList[1:]) # zip returns all tuple pairs from given inputs

def map_function(line):
    wordList = line.strip().split()
    bigramList = getBigrams(wordList)
    for bigram in bigramList:
        yield (bigram[0] + '_' + bigram[1]), 1 # Yield bigram with underscore and 1

for line in sys.stdin:
    # Call the map_function for each line in the input
    for key, value in map_function(line):
        # Agregate value for a word locally
        bigramDictionary[key] += value

        # To keep O(1) space, we bound the size of our memory footprint
        if len(bigramDictionary) >= MAX_SIZE:
            for key, value in bigramDictionary.items():
                print(key + "\t" + str(value))
            bigramDictionary.clear()

# Emit leftover key-value pairs and use '\t' as the delimiter
for key, value in bigramDictionary.items():
    print(key + "\t" + str(value))
