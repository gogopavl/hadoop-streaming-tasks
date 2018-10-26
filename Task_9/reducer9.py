#!/usr/bin/python2.7
# reducer9.py
import sys

prev_key = None
value_total = 0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    key, value = line.split("\t", 1)
    value = int(value)

    # Remember that Hadoop sorts mapper output by key, and the reducer takes these keys sorted
    if prev_key == key:
        value_total += value
    else:
        if prev_key != None:  # Write result to stdout
            print("{0}\t{1}".format(prev_key, value_total))

        value_total = value
        prev_key = key

if prev_key == key:  # Don't forget the last key/value pair
        print("{0}\t{1}".format(prev_key, value_total))
