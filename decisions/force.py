G = 9.8
mass1 = float(input("enter the mass of the first body"))
mass2 = float(input("enter the mass of the second body"))
r = float(input("enter the distance from the first to the second bodies"))
force = (G * mass1 * mass2) / (r * r)
print("The force is: ",force)
