###
#File Name: Exception Handling
#Developer: Natasha Schumacher
#Date last modified: November 10 2019
#Description: Write class Rational and use try exception block
#Email address: natasha.schumacher@student.vvc.edu
###
class Rational:
 def __init__(self, numerator=0, denominator=1):
    self.numerator = numerator
       self.denominator = denominator
       try:
         denominator = 0
       except ValueError:
           print('Denominator cannot be 0.')
            
            num1 = Rational(4,8)
            print(num1.numerator/num1.denominator)

