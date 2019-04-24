"""(1) Output a menu of automotive services and the corresponding cost of each service. (2 pts) 

Ex:

Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12
"""
services = {
"Oil change" : 35.0,
"Tire rotation" : 19.0,
"Car wash" : 7.0,
"Car wax" : 12.0
}

# print the menu
print("Davy's auto shop services")
print("%s -- $%d"%("Oil change",services["Oil change"]))
print("%s -- $%d"%("Tire rotation",services["Tire rotation"]))
print("%s -- $%d"%("Car wash",services["Car wash"]))
print("%s -- $%d"%("Car wax",services["Car wax"]))

"""
2) Prompt the user for two services from the menu. (2 pts)

Ex:

Select first service:
Oil change
Select second service:
Car wax

"""

service1 = input("Select first service:")
service2 = input("Select second service:")
service1_charge = 0
service2_charge = 0

if service1 == "Oil change":
   service1_charge = 35
elif service1 == "Tire rotation":
   service1_charge = 19
elif service1 == "Car wash":
   service1_charge = 7
elif service1 == "Car wax":
   service1_charge = 12 

if service2 == "Oil change":
   service2_charge = 35
elif service2 == "Tire rotation":
   service2_charge = 19
elif service2 == "Car wash":
   service2_charge = 7
elif service2 == "Car wax":
   service2_charge = 12 

if service1 == "-":
   print("Service 1: No service")
else:
   print("Service 1: " + service1 + ", $" + str(service1_charge))

if service2 == "-":
   print("Service 2: No service")
else:
   print("Service 2: " + service2 + ", $" + str(service2_charge))

print("Total: $%d" % (service1_charge + service2_charge) )
