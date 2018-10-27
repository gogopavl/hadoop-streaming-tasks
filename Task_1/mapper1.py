#!/usr/bin/env python2
# mapper1.py
import sys
from collections import defaultdict

totalWords = 0
totalLines = 0

def map_function(line):
    numberOfWordsPerLine = len(line.strip().split()) # Get the number of totalWords in line
    yield numberOfWordsPerLine, 1 # Emit number of totalWords, 1 (number of totalLines)

for line in sys.stdin:
    # Call the map_function for each line in the input
    for counter, (key, value) in enumerate(map_function(line)):
        # Agregate value for a word locally
        totalWords += int(key)
        totalLines += int(value)

# Emit leftover key-value pairs and use '\t' as the delimiter
print(str(totalWords) + "\t" + str(totalLines))
