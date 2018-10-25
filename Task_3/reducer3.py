#!/usr/bin/python2.7
# reducer3.py
import sys

numberOfActors_total = 0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    key, value = line.split("\t", 1)
    numberOfActors = int(value)

    numberOfActors_total += numberOfActors

print("{0}".format(numberOfActors_total))
