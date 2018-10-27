#!/usr/bin/env python2
# mapper10.py
import sys
from collections import defaultdict

def map_function(line):
    splitLine = line.split("\t")
    numberOfFields = len(splitLine)
    if (numberOfFields == 9):
        titleId = splitLine[0].strip()
        releaseYear = splitLine[5].strip()
        if (releaseYear != "\N") and (int(releaseYear) >= 2010) and (int(releaseYear) <= 2018):
            yield titleId + ".0", releaseYear # If it is a year add ".0" after id - useful secondary sorting
    else:
        nameId =  splitLine[0].strip()
        titleIds = splitLine[5].strip()
        if titleIds != "\N":
            for titleId in titleIds.split(","):
                yield titleId + ".1", nameId # If it is crew add ".1" after id - useful secondary sorting

for line in sys.stdin:
    # Call the map_function for each line in the input
    for key, value in map_function(line):
        print(key + "\t" + value)
