#!/usr/bin/env python2
# taks8/mapper1.py
import sys
from collections import defaultdict

def map_function(line):
    """For a given record emits (key, value) pair where key = title id and value = either title rating or title release year

    Parameters
    ----------
    line : String type
        A line from the input stream

    Returns
    -------
    (key, value) : Tuple
        Title id and year or rating
    """
    splittedLine = line.split("\t")
    numberOfFields = len(splittedLine)
    if (numberOfFields == 9):
        titleId = splittedLine[0]
        releaseYear = splittedLine[5]
        if "\N" not in releaseYear:
            yield titleId, releaseYear
    else:
        titleId = splittedLine[0]
        rating = splittedLine[1]
        if "\N" not in rating:
            yield titleId, rating

for line in sys.stdin:
    for key, value in map_function(line):
        print(key + "\t" + value)
