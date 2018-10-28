#!/usr/bin/python2.7
# task7/reducer.py
import sys

totalWriters = 0
totalNumber = 0

for line in sys.stdin:
    key, value = line.strip().split("\t", 1)
    totalWriters += int(key)
    totalNumber += int(value)

globalAverage = float(totalWriters) / float(totalNumber)
print("{}".format(int(round(float(globalAverage))))) # Write average rounded up to the closest integer
