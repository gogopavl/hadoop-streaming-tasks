#!/usr/bin/python2.7
# reducer1.py
import sys

totalWords = 0
totalLines = 0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    words, lines = line.split("\t", 1)
    words = int(words)
    lines = int(lines)

    totalWords += words
    totalLines += lines

print("{0}\t{1}".format(totalWords, totalLines))
