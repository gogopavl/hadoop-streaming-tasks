#!/usr/bin/env python2
# mapper8.py
import sys
from collections import defaultdict

def map_function(line):
    splittedLine = line.split("\t")
    numberOfFields = len(splittedLine)
    if (numberOfFields == 9):
        titleId = splittedLine[0]
        releaseYear = splittedLine[5]
        yield titleId, releaseYear # If it is a year add ".0" after id - useful secondary sorting
    else:
        titleId = splittedLine[0]
        rating = splittedLine[1]
        yield titleId, rating # If it is a rating add ".1" after id - useful secondary sorting

for line in sys.stdin:
    for key, value in map_function(line):
        if value == "\N": # Skip these entries
            continue
        else:
            print(key + "\t" + value)
