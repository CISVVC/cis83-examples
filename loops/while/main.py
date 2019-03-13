#!/usr/bin/env python3
import random


# demonstrate the while loop
#            0 1 2 3 4 5 
diecounts = [0,0,0,0,0,0]
count = 0
while count < 100000:
   r = random.randint(1,6)

   diecounts[r-1] += 1
   count += 1

print(diecounts)
