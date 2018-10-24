#!/usr/bin/env python2
# mapper1.py
import sys
from collections import defaultdict

words = 0
lines = 0
MAX_SIZE = 100

def map_function(line):
    numberOfWordsPerLine = len(line.strip().split()) # Get the number of words in line
    yield numberOfWordsPerLine, 1 # Emit number of words, 1 (number of lines)

for line in sys.stdin:
    # Call the map_function for each line in the input
    for counter, (key, value) in enumerate(map_function(line)):
        # Agregate value for a word locally
        words += int(key)
        lines += int(value)

        # To keep O(1) space, we bound the size of our memory footprint
        if counter == MAX_SIZE:
            print(str(words) + "\t" + str(lines))
            words = 0
            lines = 0

# Emit leftover key-value pairs and use '\t' as the delimiter
print(str(words) + "\t" + str(lines))
