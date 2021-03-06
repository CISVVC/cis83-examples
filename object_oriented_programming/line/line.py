#!/usr/bin/env python3

from point import Point


class Line:

    # constructor for the Line
    # takes 2 parameters p1 and p2 both of
    # them are points

    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return self.p1.distance(self.p2)

    def __repr__(self):
        return f'<Line:{self.p1}-{self.p2}-length-{self.length():.2f}>'

if __name__ == "__main__":
    
    l1 = Line(Point(1,1),Point(2,2))
    print(l1.length())

    #print(f'{l1}')
