
def print_params(*args):

   for p in args:
      print(p)

print_params(1,2,3,4,5)
print_params('a','b','c')

def keyed_parameters(**kwargs):
   for p in kwargs:
      print(p,kwargs[p])



keyed_parameters(p1='abc',p2='cde')
keyed_parameters(p2='abc',p1='cde',p3=1234)
