#!/usr/bin/python2.7
# reducer4.py
import sys

prev_word = None

for line in sys.stdin:          # For every line in the input from stdin
    word = line.strip()         # Remove trailing characters

    if prev_word == word:
        continue
    else:
        if prev_word != None:  # Write result to stdout
            print("{0}".format(prev_word))
        prev_word = word

if prev_word == word:  # Don't forget the last key/value pair
    print("{0}".format(prev_word))
