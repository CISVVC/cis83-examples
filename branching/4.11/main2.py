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
"Car wax" : 12.0,
"-" : "No service"
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

if service1 != "-":
   service1_charge = services[service1] 
if service2 != "-":
   service2_charge = services[service2] 

print("Total: $%d" % () )
