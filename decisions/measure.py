print('Do the five cuts')
A = float(input('Enter the measure of A:'))
B = float(input('Enter the measure of B:'))
length = float(input('Enter the length of the part:'))
fence_length = float(input('Enter the fence length :'))

error_ratio = (A - B) / 4.0 / length * fence_length

if error_ratio < 0:
   print('Fence is down, move it up ',error_ratio)
else:
   print('Fence is up, move it down ',error_ratio)
