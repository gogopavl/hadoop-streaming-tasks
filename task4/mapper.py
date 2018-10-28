#!/usr/bin/env python2
# task4/mapper.py
import sys
from collections import defaultdict

genreSet = set() # Structure to temporarily save genres
MAX_SIZE = 500 # Variable to limit set size - O(1) memory complexity

def map_function(line):
    """For a given record emit its genres, if listed

    Parameters
    ----------
    line : String type
        A line from the input stream

    Returns
    -------
    genre : String
        The genre listed within the record
    """
    genres = line.split("\t")[8].strip().split(",")
    for genre in genres:
        if "\N" not in genre: # Skip these values
            yield genre # Emit genre

for line in sys.stdin:
    for key in map_function(line):
        genreSet.add(key)

        if len(genreSet) >= MAX_SIZE: # When structure reaches MAX_SIZE print and then clear it
            for genre in genreSet:
                print(genre)
            genreSet.clear()

for genre in genreSet: # Emit leftover genres
    print(genre)
genreSet.clear()
