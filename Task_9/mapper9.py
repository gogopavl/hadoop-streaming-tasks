#!/usr/bin/env python2
# mapper9.py
import sys

from collections import defaultdict

genreReleases = defaultdict(int) # Structure to temporarily save bigram terms
MAX_SIZE = 500

def map_function(line):
    fields = line.strip().split("\t")
    genres = fields[8].strip().split(",")
    releaseYear = fields[5].strip()
    for genre in genres:
        yield genre, releaseYear # Yield bigram with underscore and 1

    # if (1900 <= releaseYear) and (releaseYear <= 1999):


for line in sys.stdin:
    # Call the map_function for each line in the input
    for key, value in map_function(line):
        # Agregate value for a word locally
        if (key != "\N") and (value != "\N"):
            releaseYear = int(value)
            if (2000 <= releaseYear) and (releaseYear <= 2014):
                genreReleases[key] += 1
        # To keep O(1) space, we bound the size of our memory footprint
        if len(genreReleases) >= MAX_SIZE:
            for key, value in genreReleases.items():
                print(key + "\t" + str(value))
            genreReleases.clear()

# Emit leftover key-value pairs and use '\t' as the delimiter
for key, value in genreReleases.items():
    print(key + "\t" + str(value))
