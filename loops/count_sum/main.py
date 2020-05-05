import random

rolls = [0,0,0,0,0,0,0,0,0,0,0,0,0]

rolls[12] += 1
rolls[12] += 1
rolls[12] += 1
rolls[2] += 1
rolls[2] += 1
rolls[2] += 1
print(rolls)


value = [random.randint(1,10000) for x in range(100000)]

count = 0
for f in value:
  if f >= 8000 and f <= 10000:
     count += 1
print(count)


values2 = [random.randint(1,1000) for x in range(1000)]

total = 0
for f in values2:
   total += f
print(total)
print(total/len(values2))
