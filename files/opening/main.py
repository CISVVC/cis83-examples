#!/usr/bin/env python3

filename = "mbox.txt"

def open_file(fname):
    fhand = open(fname)
    return fhand

fhand  = open_file(filename)

count = 0

for line in fhand:
    count += 1

print(count)
