import csv


#with open('people.csv', newline='') as csvfile:
#   persons = csv.reader(csvfile, delimiter=',')
#   for person in persons:
#      print('id = {}'.format(person[0]))
#      print('lastname = {}'.format(person[1]))
#      print('firstname = {}'.format(person[2]))
#      print('type = {}'.format(person[3]))
#      print()
class Employee:
   
   def __init__(self,idnumber,lastname,firstname,position):
      self.id = idnumber
      self.lastname = lastname
      self.firstname = firstname
      self.position = position

   def __str__(self):
      return "id={},lastname={},firstname={},position={}".format(
                  self.id,
                  self.lastname,
                  self.firstname,
                  self.position)


csvfile = open('people.txt', newline='')
employee_list = []
for idnumber,lastname,firstname,position in csv.reader(csvfile, delimiter=','):
    e = Employee(idnumber,lastname,firstname,position)
    print(e)
    employee_list.append(e)
