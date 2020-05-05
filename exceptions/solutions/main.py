class Rational:
   
   def __init__(self,num,denom):
      
      self.num = num
      if denom == 0:
         raise Exception("denominator cannot be 0")
      self.denom = denom


try:
   rat = Rational(1,0)
except Exception as e:
   print(e)
