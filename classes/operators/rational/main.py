class Rational:
   
   def __init__(self,n,d):
      self.numerator = n
      self.denominator = d

   def __add__(self,r):
      
      denominator = r.denominator * self.denominator
      numerator = r.numerator * self.denominator + self.numerator * r.denominator

      return Rational(numerator,denominator)

   def __str__(self):
      return str(self.numerator) + "/" + str(self.denominator)


r1 = Rational(10,15)
r2 = Rational(25,30)

print(r1 + r2)
