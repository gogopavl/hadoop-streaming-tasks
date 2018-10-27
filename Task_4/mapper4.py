#!/usr/bin/env python2
# mapper4.py
import sys
from collections import defaultdict

genreSet = set()
<<<<<<< HEAD
MAX_SIZE = 500
=======
MAX_SIZE = 100
>>>>>>> c6849e9bded7996b647936969a736cc117dfe8fc

def map_function(line):
    genres = line.split("\t")[8].strip().split(",")
    for genre in genres:
        if genre != "\N":
            yield genre # Emit key 1 - same reducer, 1 (occurence of actor/actress)

for line in sys.stdin:
    # Call the map_function for each line in the input
    for key in map_function(line):
        # To keep O(1) space, we bound the size of our memory footprint
        genreSet.add(key)
        if len(genreSet) >= MAX_SIZE:
            for genre in genreSet:
                print(genre)
            genreSet.clear()

# Emit leftover key-value pairs and use '\t' as the delimiter
for genre in genreSet:
    print(genre)
genreSet.clear()
