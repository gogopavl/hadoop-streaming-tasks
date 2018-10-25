#!/usr/bin/env python2
# mapper5.py
import sys
from collections import defaultdict

earliestYear = 20000
latestYear = -20000

def map_function(line):
    releaseYear = line.split("\t")[5].strip()
    yield releaseYear

for line in sys.stdin:
    # Call the map_function for each line in the input
    for year in map_function(line):
        # To keep O(1) space, we bound the size of our memory footprint
        if year == "\N": # Skip this value
            continue

        intYear = int(year)

        if intYear < earliestYear:
            earliestYear = intYear
        if intYear > latestYear:
            latestYear = intYear
            
print(str(earliestYear) + "\t" + str(latestYear))
