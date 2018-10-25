#!/usr/bin/python2.7
# reducer4.py
import sys

for line in sys.stdin:          # For ever line in the input from stdin
    key = line.strip()         # Remove trailing characters
    print("{0}".format(key))
