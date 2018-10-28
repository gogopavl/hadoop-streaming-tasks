#!/usr/bin/python2.7
# task4/reducer.py
import sys

prev_genre = None

for line in sys.stdin:
    genre = line.strip()

    if prev_genre == genre:
        continue
    else:
        if prev_genre != None:  # Write result to stdout
            print("{0}".format(prev_genre))
        prev_genre = genre

if prev_genre == genre: # Emit the last genre
    print("{0}".format(prev_genre))
