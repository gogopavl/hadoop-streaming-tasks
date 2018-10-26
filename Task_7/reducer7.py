#!/usr/bin/python2.7
# reducer7.py
import sys

partialAverage = 0
totalNumber = 0

for line in sys.stdin:          # For ever line in the input from stdin
    key = line.strip()         # Remove trailing characters
    partialAverage += float(key)
    totalNumber += 1

globalAverage = partialAverage / totalNumber
print("{}".format(int(round(globalAverage))))
