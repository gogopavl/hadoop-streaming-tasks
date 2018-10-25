#!/usr/bin/env python2
# mapper3.py
import sys
from collections import defaultdict

numberOfActors = 0
MAX_SIZE = 100

def map_function(line):
    primaryProfession = line.split("\t")[4]
    if "actor" in primaryProfession or "actress" in primaryProfession:
        yield 1, 1 # Emit key 1 - same reducer, 1 (occurence of actor/actress)

for line in sys.stdin:
    # Call the map_function for each line in the input
    for counter, (key, value) in enumerate(map_function(line)):
        # Agregate value for a word locally
        numberOfActors += value

        # To keep O(1) space, we bound the size of our memory footprint
        if counter == MAX_SIZE:
            print(str(1) + "\t" + numberOfActors)
            numberOfActors = 0

# Emit leftover key-value pairs and use '\t' as the delimiter
print(str(1) + "\t" + str(numberOfActors))
