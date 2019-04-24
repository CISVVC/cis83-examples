import math
def hypot(**kwargs):
   
   print('leg1 is ',kwargs['leg1'],'leg2 is ',kwargs['leg2'])
   return math.sqrt(kwargs['leg1'] ** 2 + kwargs['leg2'] ** 2)


print(hypot(leg1=2,leg2=3))
print(hypot(leg2=2,leg1=3))
