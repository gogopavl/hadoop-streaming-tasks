#!/usr/bin/env python2
# mapper3.py
import sys
from collections import defaultdict

totalWriters = 0
totalTitles = 0

def map_function(line):
    stringOfWriters = line.split("\t")[2].strip()
    listOfWriters = stringOfWriters.split(",")
    numOfWriters = len(listOfWriters)
    yield numOfWriters, 1

for line in sys.stdin:
    # Call the map_function for each line in the input
    for key, value in map_function(line):
        if key == "\N": # Skip these entries
            continue
        totalWriters += key
        totalTitles += value

average = float(totalWriters) / totalTitles
print(str(average))
