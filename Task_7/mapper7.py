#!/usr/bin/env python2
# mapper3.py
import sys
from collections import defaultdict

totalWriters = 0
totalTitles = 0

def map_function(line):
    ident = line.split("\t")[0].strip()
    stringOfWriters = line.split("\t")[2].strip()
    listOfWriters = stringOfWriters.split(",")
    if "\N" not in listOfWriters:
        numOfWriters = len(listOfWriters)
        if numOfWriters >= 1:
            yield numOfWriters, 1

for line in sys.stdin:
    # Call the map_function for each line in the input
    for key, value in map_function(line):
        totalWriters += key
        totalTitles += value

# average = float(totalWriters) / totalTitles
print(str(totalWriters) + "\t" + str(totalTitles))
