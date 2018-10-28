#!/usr/bin/env python2
# task9/mapper.py
import sys

from collections import defaultdict

genreReleases = defaultdict(int) # Structure to temporarily save genres
MAX_SIZE = 500 # Variable to limit dictionary size - O(1) memory complexity

def map_function(line):
    """For a given record emits (key, value) pair where key = genre and value = the release year within a certain range

    Parameters
    ----------
    line : String type
        A line from the input stream

    Returns
    -------
    (key, value) : Tuple
        The genre and year of release
    """
    fields = line.strip().split("\t")
    genres = fields[8].strip().split(",")
    releaseYear = fields[5].strip()
    if "\N" not in releaseYear and "\N" not in genres:
        releaseYear = int(releaseYear)
        if (2000 <= releaseYear) and (releaseYear <= 2014):
            for genre in genres:
                yield genre, releaseYear

for line in sys.stdin:
    for key, value in map_function(line):
        genreReleases[key] += 1

        if len(genreReleases) >= MAX_SIZE:
            for key, value in genreReleases.iteritems():
                print(key + "\t" + str(value))
            genreReleases.clear()

for key, value in genreReleases.items():
    print(key + "\t" + str(value))
