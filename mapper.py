#!/usr/bin/env python2
# mapper.py
import sys

def map_function(document):
    # Split document by words and use word as the key
    for word in document.strip().split():
        yield word, 1

for line in sys.stdin:
    # Call map_function for each line in the input
    for key, value in map_function(line):
        # Emit key-value pairs using '\t' as a delimeter
        print(key + "\t" + str(value))
