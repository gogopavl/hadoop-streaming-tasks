#!/usr/bin/env python2
# task10/mapper.py
import sys
from collections import defaultdict

def map_function(line):
    """For a given record emits (key, value) pair where key = title id and value = the release year within a certain range.
    ".0" is appended to the id if it is a year entry and ".1" if it's a name entry. This helps sorting, since the job is
    run using secondary sorting.

    Parameters
    ----------
    line : String type
        A line from the input stream

    Returns
    -------
    (key, value) : Tuple
        Title id and year or title id and name id
    """
    splitLine = line.split("\t")
    numberOfFields = len(splitLine)
    if (numberOfFields == 9):
        titleId = splitLine[0].strip()
        releaseYear = splitLine[5].strip()
        if (releaseYear != "\N") and (int(releaseYear) >= 2010) and (int(releaseYear) <= 2018):
            yield titleId + ".0", releaseYear # If it is a year add ".0" after id - useful for secondary sorting
    else:
        nameId =  splitLine[0].strip()
        titleIds = splitLine[5].strip()
        if titleIds != "\N":
            for titleId in titleIds.split(","):
                yield titleId + ".1", nameId # If it is crew add ".1" after id - useful for secondary sorting

for line in sys.stdin:
    for key, value in map_function(line):
        print(key + "\t" + value)
