#!/usr/bin/env python3

filename = input("Enter the file name:")

def open_file(fname):
    fhand = open(fname)
    return fhand

fhand  = open_file(filename)

count = 0

for line in fhand:
    line = line.rstrip()

    if not line.startswith('From:'):
        count += 1
        continue

    print(line)

print(count)
