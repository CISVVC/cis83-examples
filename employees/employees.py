class Employee():
    
   def __init__(self,idnumber,name):
      self.idnumber = idnumber
      self.name = name

   def get_id(self): 
      return self.idnumber
    
class ProductionWorker(Employee):

   def __init__(self,idnumber,name,shift,payrate,hours):
      Employee.__init__(self,idnumber,name)
      self.shift = shift
      self.payrate = payrate
      self.hours = hours


class ShiftManager():

   def __init__(self,employees = None):
      self.employees = employees

   def add_emp(self,e):
      self.employees[e.id] = e
       
