import random
values = ([random.randint(1,100000) for x in range(1000000)])
values.sort()


print(values[-1])
print(values[0])

