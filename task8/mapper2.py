#!/usr/bin/env python2
# task8/mapper2.py
import sys
from collections import defaultdict

def map_function(line):
    """For a given (key, value) pair transforms year into decade and emits (key, value) pairs where key = decade and value = rating

    Parameters
    ----------
    line : String type
        A line from the input stream

    Returns
    -------
    (key, value) : Tuple
        Decade and rating
    """
    line = line.strip()
    key, value = line.split("\t")
    tempList = list(key)
    tempList[-1] = '0'
    key = "".join(tempList)
    yield key, value

for line in sys.stdin:
    for key, value in map_function(line):
        print("{0}\t{1}".format(key, value))
