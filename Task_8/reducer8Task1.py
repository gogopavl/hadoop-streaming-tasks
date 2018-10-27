#!/usr/bin/python2.7
# reducer8.py
import sys

prev_key = None
prev_value = None

for line in sys.stdin:          # For ever line in the input from stdin
    strippedLine = line.strip()         # Remove trailing characters
    key, value = strippedLine.split("\t", 1)

    if prev_key == key:
        # check and assing correct values
        if ("." in prev_value):
            if (int(value) > 1899) and (int(value) < 2000):
                print("{0}\t{1}".format(value, prev_value))
        else:
            if (int(prev_value) > 1899) and (int(prev_value) < 2000):
                print("{0}\t{1}".format(prev_value, value))
    else:
        prev_key = key
        prev_value = value
