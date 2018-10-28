#!/usr/bin/python2.7
# task6/reducer.py
import sys

totalVotes = 0
totalNumber = 0

for line in sys.stdin:
    key, value = line.strip().split("\t",1)

    totalVotes += int(key)
    totalNumber += int(value)

globalAverage = float(totalVotes) / float(totalNumber)
print("{0:.2f}".format(round(float(globalAverage),2))) # Rounded up to 2 decimal places
