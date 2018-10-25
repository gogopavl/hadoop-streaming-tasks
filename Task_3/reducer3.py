#!/usr/bin/python2.7
# reducer3.py
import sys

numberOfActors_total = 0

for line in sys.stdin:          # For ever line in the input from stdin
    key = line.strip()         # Remove trailing characters
    numberOfActors = int(key)
    numberOfActors_total += numberOfActors

print("{0}".format(numberOfActors_total))
