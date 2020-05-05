from employees import (
ProductionWorker,ShiftManager
)

# declare a dictionary
# open the csv file
# iterate over the file
# add to the dictionary

employees = {}

e = ProductionWorker('2','Barney Rubble',2,18,40)
employees[e.get_id()] = e
e = ProductionWorker('1','Fred Flintstone',1,15,40)
employees[e.get_id()] = e

#keys = list(employees)
#keys.sort()
new_dict = {}
for key in sorted(employees):
   #print("key = {}".format(key),"employee = {}".format(employees[key]))
   new_dict[key] = employees[key]
   #print("key = {}".format(key),"employee = {}".format(value))

for key,value in new_dict.items():
   print("key = {}".format(key),"employee = {}".format(value))

