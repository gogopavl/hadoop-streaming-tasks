#!/usr/bin/python2.7
# task1/reducer.py
import sys

totalWords = 0 # Global variable for the number of words - O(1)
totalLines = 0 # Global variable for the number of lines - O(1)

for line in sys.stdin:
    line = line.strip()
    words, lines = line.split("\t", 1)
    words = int(words)
    lines = int(lines)

    totalWords += words
    totalLines += lines

print("{0}\t{1}".format(totalWords, totalLines))
