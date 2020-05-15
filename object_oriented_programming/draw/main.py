#!/usr/bin/env python3
import math
import line
import point

def getCanvas(c,rows,cols):
    return [[c]*cols for i in range(rows)]


def main():
    canvas = getCanvas(' ',25,90)
    rect = [ line.Line(point.Point(1,6),point.Point(6,6)),
             line.Line(point.Point(6,6),point.Point(6,1)),
             line.Line(point.Point(6,1),point.Point(1,1)),
             line.Line(point.Point(1,1),point.Point(1,6))
            ]
    for l in rect:
        l.draw(canvas)

if __name__ == '__main__':
    main()
