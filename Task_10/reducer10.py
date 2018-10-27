#!/usr/bin/python2.7
# reducer10.py
import sys

titleIdToWrite = None

for line in sys.stdin: # For ever line in the input from stdin
    strippedLine = line.strip() # Remove trailing characters

    key, value = strippedLine.split("\t", 1)
    keyParts = key.split(".")
    splitKey = keyParts[0]
    splitKeyType = keyParts[1]

    if splitKeyType == "0":
        titleIdToWrite = splitKey
    else:
        if splitKey == titleIdToWrite:
            print("{0}".format(value))

#     if prev_key == titleIdToWrite:
#         print("{0}".format(value))
#     else:
#         keyParts = key.split(".")
#         splitKey = keyParts[0]
#         splitKeyType = keyParts[1]
#         print('type {}'.format(splitKeyType))
#         if splitKeyType == "0":
#             titleIdToWrite = splitKey
#
#         prev_key = splitKey
#         prev_value = value
#
# if prev_key == titleIdToWrite: # Last pair
#     # check and assing correct values
#     print("{0}".format(value))
