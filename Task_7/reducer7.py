#!/usr/bin/python2.7
# reducer7.py
import sys

totalWriters = 0
totalNumber = 0

for line in sys.stdin:          # For ever line in the input from stdin
    key, value = line.strip().split("\t", 1)         # Remove trailing characters
    totalWriters += int(key)
    totalNumber += int(value)

globalAverage = float(totalWriters) / float(totalNumber)
# print("{}".format(globalAverage))
print("{}".format(int(round(float(globalAverage)))))
