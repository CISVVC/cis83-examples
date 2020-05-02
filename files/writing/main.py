#!/usr/bin/env python3

ifilename = input("Enter the input file name:")
ofilename = input("Enter the output file name:")

def open_file(fname,mode):
    try:
        fhand = open(fname,mode)
    except:
        print('File cannot be opened',fname)
        exit(1)

    return fhand

fhand_input  = open_file(ifilename,'r')
fhand_output  = open_file(ofilename,'w')

count = 0

for line in fhand_input:

    if not line.startswith('From:'):
        count += 1
        continue

    fhand_output.write(line)

fhand_output.close()
print(count)
