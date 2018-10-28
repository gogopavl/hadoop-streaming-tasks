#!/usr/bin/env python2
# task6/mapper.py
import sys
from collections import defaultdict

totalVotes = 0
totalNum = 0

def map_function(line):
    """For a given record emits (key, value) pair where key = number of votes and value = 1

    Parameters
    ----------
    line : String type
        A line from the input stream

    Returns
    -------
    (key, value) : Tuple
        The number of votes and 1 - single occurrence
    """
    votes = line.split("\t")[2].strip()
    if "\N" not in votes: # Skip this record
        votes = int(votes)
        yield votes, 1

for line in sys.stdin:
    for key, value in map_function(line):
        totalVotes += key
        totalNum += value

print(str(totalVotes) +"\t"+ str(totalNum))
