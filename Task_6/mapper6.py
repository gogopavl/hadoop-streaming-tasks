#!/usr/bin/env python2
# mapper6.py
import sys
from collections import defaultdict

totalVotes = 0
totalNum = 0

def map_function(line):
    votes = line.split("\t")[2].strip()
    if votes != "\N":
        votes = int(votes)
        yield votes, 1

for line in sys.stdin:
    for key, value in map_function(line):
        totalVotes += key
        totalNum += value

print(str(totalVotes) +"\t"+ str(totalNum))
