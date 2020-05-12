#!/usr/bin/env python3
import math
from line.line import Line
from line.point import Point

def plot(canvas,x,y):
    canvas[y][x] = '.'

def printCanvas(c):
    print('0123456789'*(len(c[0])//10))
    for idx,l in enumerate(c):
        print(str((len(c)-idx)%10)+"".join(l))
    print('0123456789'*(len(c[0])//10))

def getCanvas(c,rows,cols):
    return [[c]*cols for i in range(rows)]

# variation of the Bresenham Line Drawing algorithm
def plotLine(x0, y0, x1, y1):
    canvas = getCanvas(' ',25,90)
    dx =  abs(x1-x0)
    if x0<x1:
        sx = 1
    else:
        sx = -1
    dy = -abs(y1-y0)
    if y0<y1:
        sy = 1
    else:
        sy = -1
    err = dx+dy  # error value e_xy
    while True:  # loop
        plot(canvas,x0, y0)
        if x0==x1 and y0==y1:
            break
        e2 = 2*err
        if e2 >= dy:
            err += dy   # e_xy+e_x > 0
            x0 += sx
        if e2 <= dx:     # e_xy+e_y < 0 
            err += dx
            y0 += sy

    return canvas


if __name__ == "__main__":
    printCanvas(plotLine(10, 10, 25, 2))
