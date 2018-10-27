#!/usr/bin/python2.7
# reducer6.py
import sys

totalVotes = 0
totalNumber = 0

for line in sys.stdin:          # For ever line in the input from stdin
    key, value = line.strip().split("\t",1)         # Remove trailing characters

    totalVotes += int(key)
    totalNumber += int(value)

globalAverage = float(totalVotes) / float(totalNumber)
print("{0:.2f}".format(round(float(globalAverage),2)))
