#!/usr/bin/env python3

import math
import line
import point

def getCanvas(c,rows,cols):
    return [[c]*cols for i in range(rows)]

class Rect():
    def __init__(self,ul,lr):
        p = point.Point
        self.rect = [ 
                 line.Line(ul,p(lr.x,ul.y)),
                 line.Line(p(lr.x,ul.y),p(lr.x,lr.y)),
                 line.Line(p(lr.x,lr.y),p(ul.x,lr.y)),
                 line.Line(p(ul.x,lr.y),p(ul.x,ul.y)), ]

    def draw(self,canvas):
        for l in self.rect:
            l.plotLine(canvas)
        l.printCanvas(canvas)


def main():
    p = point.Point
    canvas = getCanvas(' ',25,90)
    r = Rect(p(1,6),p(6,1))
    r.draw(canvas)


if __name__ == '__main__':
    main()
