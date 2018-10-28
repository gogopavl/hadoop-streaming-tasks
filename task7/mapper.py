#!/usr/bin/env python2
# task7/mapper.py
import sys
from collections import defaultdict

totalWriters = 0
totalTitles = 0

def map_function(line):
    """For a given record emits (key, value) pair where key = number of writers and value = 1

    Parameters
    ----------
    line : String type
        A line from the input stream

    Returns
    -------
    (key, value) : Tuple
        The number of writers and 1 - single occurrence
    """
    stringOfWriters = line.split("\t")[2].strip()
    listOfWriters = stringOfWriters.split(",")
    if "\N" not in listOfWriters:
        numOfWriters = len(listOfWriters)
        if numOfWriters >= 1:
            yield numOfWriters, 1

for line in sys.stdin:
    for key, value in map_function(line):

        totalWriters += key
        totalTitles += value

print(str(totalWriters) + "\t" + str(totalTitles))
