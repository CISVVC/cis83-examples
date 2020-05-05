#!/usr/bin/env python3
import math

#(1,1)  ---->  (3,4)

def distance(x1,y1,x2,y2):
    d = math.sqrt( (x2-x1)**2 + (y2-y1) ** 2);
    return d

print(distance(1,1,3,4))
print(distance(2,1,4,5))
