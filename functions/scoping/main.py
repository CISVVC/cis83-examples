x = 10
y = 100

def f1(myvariable):
   y = x * 1000
   print(myvariable)
   print(y)

print("x before call to f1",x)

f1(x)

print("x after call to f1",x)
