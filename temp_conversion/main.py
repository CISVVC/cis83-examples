'''
get the degree value from user assign it to deg
get the conversion type and set it to conv_type (1 for F->C and 2 for C->F)
if conv_type == 1:
   converted_value = 9 / 5 * deg + 32
else
   converted_value = 5 / 9 *(deg - 32)

print converted_value 
'''

deg = float(input('Enter the degree value: '))
conv_type = input('Enter F2C for F->C or C2F for C->F: ')
if conv_type.upper() == 'F2C'
   converted_value = 5/9 * (deg - 32)
elif conv_type.upper() == 'C2F':
   converted_value = 9 / 5 * deg + 32
else:
   print("invalid conversion type")

print(converted_value)
