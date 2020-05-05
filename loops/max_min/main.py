import random
values = [random.randint(1,100000) for x in range(1000000)]

def my_max(lst):
   max_num = lst[0]
   for i in lst:
      if i > max_num:
         max_num = i
   return max_num

def my_min(lst):
   num = lst[0]
   for i in lst:
      if i < num:
         num = i
   return num

print(my_max(values))
print(my_min(values))

