#!/usr/bin/env python3
import math

class Point:
   '''
   Point class demonstrates modeling a Cartesian point
   '''
   # Constructor
   def __init__(self,x,y):
       self.x = x
       self.y = y
    
   def distance(self,otherpoint):
       return math.sqrt((self.x - otherpoint.x)**2+(self.y-otherpoint.y)**2)

   def __repr__(self):
       return f'({self.x},{self.y})'

if __name__ == '__main__':

   p1 = Point(1,1)
   p2 = Point(2,2)
   
   print(f'The distance between {p1} and {p2} is {p1.distance(p2):.2f}')

   
