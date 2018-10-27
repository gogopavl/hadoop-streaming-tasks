#!/usr/bin/python2.7
# reducer8_2.py
import sys

prev_key = None
prev_value = None

sumTotal = 0.0
counter = 1

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    key, value = line.split("\t", 1)
    key = int(key)
    value = float(value)

    if prev_key == key:
        sumTotal += value
        counter += 1
    else:
        if prev_key != None:
            averageRating = float(sumTotal) / float(counter)
            print("{0}\t{1:.1f}".format(prev_key, round(float(averageRating),1)))

        prev_key = key
        prev_value = value
        sumTotal = value
        counter = 1

if prev_key == key:  # Don't forget the last key/value pair
    averageRating = float(sumTotal) / float(counter)
    print("{0}\t{1:.1f}".format(prev_key, round(float(averageRating),1)))
