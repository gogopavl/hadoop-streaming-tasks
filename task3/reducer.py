#!/usr/bin/python2.7
# task3/reducer.py
import sys

numberOfActors_total = 0

for line in sys.stdin:
    key = line.strip()
    numberOfActors = int(key)
    numberOfActors_total += numberOfActors

print("{0}".format(numberOfActors_total))
