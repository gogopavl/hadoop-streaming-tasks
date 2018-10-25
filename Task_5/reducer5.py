#!/usr/bin/python2.7
# reducer5.py
import sys

earliestYearGlobal = 20000
latestYearGlobal = -20000

for line in sys.stdin:          # For ever line in the input from stdin
    pair = line.split("\t", 1)
    earliestYear = int(pair[0])
    latestYear = int(pair[1])

    if earliestYear < earliestYearGlobal:
        earliestYearGlobal = earliestYear
    if latestYear > latestYearGlobal:
        latestYearGlobal = latestYear

print("{0}\t{1}".format(earliestYearGlobal, latestYearGlobal))
