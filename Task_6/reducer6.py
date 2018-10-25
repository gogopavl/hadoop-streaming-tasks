#!/usr/bin/python2.7
# reducer3.py
import sys

partialAverage = 0
totalNumber = 0

for line in sys.stdin:          # For ever line in the input from stdin
    key = line.strip()         # Remove trailing characters
    partialAverage += float(key)
    totalNumber += 1

globalAverage = partialAverage / totalNumber
print("{0:.2f}".format(round(float(globalAverage),2)))
