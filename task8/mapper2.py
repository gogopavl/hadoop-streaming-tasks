#!/usr/bin/env python2
# mapper8_2.py
import sys
from collections import defaultdict

def map_function(line):
    line = line.strip()
    key, value = line.split("\t")
    tempList = list(key)
    tempList[-1] = '0'
    key = "".join(tempList)
    yield key, value

for line in sys.stdin:
    # Call the map_function for each line in the input
    for key, value in map_function(line):
        print("{0}\t{1}".format(key, value))
