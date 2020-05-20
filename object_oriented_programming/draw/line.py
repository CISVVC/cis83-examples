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
    
    def plot(self,canvas,x,y,char='.'):
        canvas[y][x] = char

    def printCanvas(self,c):
#        print('0123456789'*(len(c[0])//10))
        for idx,l in enumerate(c):
#            print(str((len(c)-idx)%10)+"".join(l))
            print("".join(l))
#        print('0123456789'*(len(c[0])//10))

    def plotLine(self,canvas):
        x0 = self.p1.x
        y0 = self.p1.y
        x1 = self.p2.x
        y1 = self.p2.y
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
            self.plot(canvas,x0, y0)
            if x0==x1 and y0==y1:
                break
            e2 = 2*err
            if e2 >= dy:
                err += dy   # e_xy+e_x > 0
                x0 += sx
            if e2 <= dx:     # e_xy+e_y < 0 
                err += dx
                y0 += sy

    def draw(self,canvas):
        self.plotLine(canvas)
        self.printCanvas(canvas)

    def __repr__(self):
        return f'<Line:{self.p1}-{self.p2}-length-{self.length():.2f}>'

if __name__ == "__main__":
    
    l1 = Line(Point(1,1),Point(2,2))
    print(l1.length())

    #print(f'{l1}')
