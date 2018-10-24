#!/usr/bin/env python2
# mapper.py
import sys

from collections import defaultdict

word_dict = defaultdict(int)
MAX_SIZE = 100

def map_function(document):
    # Split document by words where word is the key
    for word in document.strip().split():
        yield word, 1

for line in sys.stdin:
    # Call the map_function for each line in the input
    for key, value in map_function(line):
        # Agregate value for a word locally
        word_dict[key] += value

        # To keep O(1) space, we bound the size of our memory footprint
        if len(word_dict) > MAX_SIZE:
            for key, value in word_dict.items():
                print(key + "\t" + str(value))

            word_dict.clear()

# Emit leftover key-value pairs and use '\t' as the delimiter
for key, value in word_dict.items():
    print(key + "\t" + str(value))
