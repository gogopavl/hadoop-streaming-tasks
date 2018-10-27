#!/usr/bin/env python2
# mapper5.py
import sys
from collections import defaultdict

earliestYear = sys.maxint
latestYear = -sys.maxint -1

def map_function(line):
    releaseYear = line.split("\t")[5].strip()
    if releaseYear != "\N": # Skip this value
        yield int(releaseYear)

for line in sys.stdin:
    for year in map_function(line):
        if year < earliestYear:
            earliestYear = year
        if year > latestYear:
            latestYear = year

print(str(earliestYear) + "\t" + str(latestYear))
