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
<<<<<<< HEAD

=======
    # print('k = {} v = {}'.format(key, value))
    # print('prev {} key {}'.format(prev_key, key))
>>>>>>> c6849e9bded7996b647936969a736cc117dfe8fc
    if prev_key == key:
        sumTotal += value
        counter += 1
    else:
        if prev_key != None:
<<<<<<< HEAD
            averageRating = float(sumTotal) / float(counter)
            print("{0}\t{1:.1f}".format(prev_key, round(float(averageRating),1)))
=======
            averageRating = sumTotal / counter
            print("{0}\t{1:.1f}".format(prev_key, round(float(averageRating),2)))
>>>>>>> c6849e9bded7996b647936969a736cc117dfe8fc

        prev_key = key
        prev_value = value
        sumTotal = value
        counter = 1

if prev_key == key:  # Don't forget the last key/value pair
<<<<<<< HEAD
    averageRating = float(sumTotal) / float(counter)
    print("{0}\t{1:.1f}".format(prev_key, round(float(averageRating),1)))
=======
    averageRating = sumTotal / counter
    print("{0}\t{1:.1f}".format(prev_key, round(float(averageRating),2)))
>>>>>>> c6849e9bded7996b647936969a736cc117dfe8fc
