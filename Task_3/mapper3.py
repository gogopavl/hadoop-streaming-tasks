#!/usr/bin/env python2
# mapper3.py
import sys
from collections import defaultdict

numberOfActors = 0
MAX_SIZE = 100

def map_function(line):
    primaryProfession = line.split("\t")[4].strip()
    if "actor" in primaryProfession or "actress" in primaryProfession:
        yield 1 # Emit key 1 - same reducer, 1 (occurence of actor/actress)

for line in sys.stdin:
    # Call the map_function for each line in the input
    for counter, key in enumerate(map_function(line)):
        # Agregate value for a word locally
        numberOfActors += key

print(str(numberOfActors))
