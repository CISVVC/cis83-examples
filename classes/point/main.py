import math

class Point:
   
   def __init__(self,x,y):
      self.x = x
      self.y = y

   def __str__(self):
      return "(" + str(self.x) + "," + str(self.y) + ")" 
   
   def distance(self,p):
      return math.sqrt((p.x-self.x ) ** 2 + (p.y-self.y) ** 2)      

   def translate(self,horiz,vert):
      #self.x = self.x + horiz
      #self.y = self.y + vert
      return Point(self.x+horiz,self.y+vert)

   def print(self):
      print(self)




if __name__ == "__main__":
   x = 10;
   p1 = Point(1,1)

   p3 = p1.translate(2,-3)

   p2 = Point(2,2)

   print(p3.distance(p2))

