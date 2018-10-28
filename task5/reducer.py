#!/usr/bin/python2.7
# task5/reducer.py
import sys

earliestYearGlobal = sys.maxint
latestYearGlobal = -sys.maxint -1

for line in sys.stdin:
    pair = line.split("\t", 1)
    earliestYear = int(pair[0])
    latestYear = int(pair[1])
    if earliestYear < earliestYearGlobal: # Check whether the releaseYear is smaller than the min of greater than the max
        earliestYearGlobal = earliestYear
    if latestYear > latestYearGlobal:
        latestYearGlobal = latestYear

print("{0}\t{1}".format(earliestYearGlobal, latestYearGlobal))
