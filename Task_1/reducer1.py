#!/usr/bin/python2.7
# reducer1.py
import sys

words_total = 0
lines_total = 0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    words, lines = line.split("\t", 1)
    words = int(words)
    lines = int(lines)

    words_total += words
    lines_total += lines

print("{0}\t{1}".format(words_total, lines_total))
