#!/usr/bin/env python2
# task5/mapper.py
import sys
from collections import defaultdict

earliestYear = sys.maxint
latestYear = -sys.maxint -1

def map_function(line):
    """For a given record emit its release year

    Parameters
    ----------
    line : String type
        A line from the input stream

    Returns
    -------
    releaseYear : Integer
        The releaseYear of the record
    """
    releaseYear = line.split("\t")[5].strip()
    if "\N" not in releaseYear: # Skip this value
        yield int(releaseYear)

for line in sys.stdin:
    for year in map_function(line): # Check whether the releaseYear is smaller than the min of greater than the max
        if year < earliestYear:
            earliestYear = year
        if year > latestYear:
            latestYear = year

print(str(earliestYear) + "\t" + str(latestYear))
