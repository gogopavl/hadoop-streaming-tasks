#!/usr/bin/env python2
# task1/mapper.py
import sys
from collections import defaultdict

totalWords = 0 # Global variable for the number of words - O(1)
totalLines = 0 # Global variable for the number of lines - O(1)

def mapFunction(line):
    """Given a line emits (key, value) pairs, where key = number of words per line and value = 1 - the number of lines

    Parameters
    ----------
    line : String type
        A line from the input stream

    Returns
    -------
    numberOfWordsPerLine, 1 : Tuple
        The sum of words within the (1) given line
    """
    numberOfWordsPerLine = len(line.strip().split()) # Number of totalWords in line
    yield numberOfWordsPerLine, 1 # Emit number of totalWords, 1 (number of totalLines)

for line in sys.stdin:
    for key, value in mapFunction(line):

        totalWords += int(key)
        totalLines += int(value)

print(str(totalWords) + "\t" + str(totalLines)) # Write result to stream
