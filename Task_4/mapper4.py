#!/usr/bin/env python2
# mapper4.py
import sys
from collections import defaultdict

genreSet = set()
MAX_SIZE = 100

def map_function(line):
    genres = line.split("\t")[8].strip().split(",")
    for genre in genres:
        if genre == "\N": # skip these values
            continue
        yield genre # Emit key 1 - same reducer, 1 (occurence of actor/actress)

for line in sys.stdin:
    # Call the map_function for each line in the input
    for key in map_function(line):
        # To keep O(1) space, we bound the size of our memory footprint
        genreSet.add(key)
        if len(genreSet) == MAX_SIZE:
            for genre in genreSet:
                print(genre)
            genreSet.clear()

# Emit leftover key-value pairs and use '\t' as the delimiter
for genre in genreSet:
    print(genre)
genreSet.clear()
