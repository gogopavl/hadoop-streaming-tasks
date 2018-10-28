#!/usr/bin/env python2
# task3/mapper.py
import sys
from collections import defaultdict

numberOfActors = 0

def map_function(line):
    """If a person's record contains "actor" or "actress" in their profession field returns 1

    Parameters
    ----------
    line : String type
        A line from the input stream

    Returns
    -------
    1 : Integer
        The occurrence
    """
    primaryProfession = line.split("\t")[4].strip()
    if ("actor" in primaryProfession) or ("actress" in primaryProfession):
        yield 1 # Emit 1 - same reducer, 1 (occurence of actor/actress)

for line in sys.stdin:
    for key in map_function(line):
        numberOfActors += key # Local sum instead of emitting each occurrence

print(str(numberOfActors))
