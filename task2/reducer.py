#!/usr/bin/python2.7
# task2/reducer.py
import sys

prev_word = None
value_total = 0

for line in sys.stdin:
    line = line.strip()

    word, value = line.split("\t", 1)
    value = int(value)

    if prev_word == word:
        value_total += value
    else:
        if prev_word != None:
            if value_total > 5: # Write only bigrams that occur more than 5 times
                print("{0}\t{1}".format(prev_word, value_total))
        value_total = value
        prev_word = word

if prev_word == word:
    if value_total > 5: # Write only bigrams that occur more than 5 times
        print("{0}\t{1}".format(prev_word, value_total))
