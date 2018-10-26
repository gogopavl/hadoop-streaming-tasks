#!/usr/bin/env python2
# mapper6.py
import sys
from collections import defaultdict


totalVotes = 0
totalNum = 0

def map_function(line):
    votes = float(line.split("\t")[2].strip())
    # check non float?
    yield votes, 1

for line in sys.stdin:
    # Call the map_function for each line in the input
    for key, value in map_function(line):
        # Agregate value for a word locally
        totalVotes += key
        totalNum += value

average = totalVotes / totalNum
print(str(average))
