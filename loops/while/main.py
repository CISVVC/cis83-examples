#!/usr/bin/env python3

countdown = 10
while countdown > 0:
   print(countdown)
   countdown = countdown - 1

countdown = 10
while True:
   if countdown >= 0:
      print(countdown)
   else:
      break
   countdown = countdown - 1

countdown = 10
while countdown > 0:
   if countdown != 4:
      print(countdown)
   else:
      countdown = countdown - 1
      continue

   countdown = countdown - 1

print("Done")

