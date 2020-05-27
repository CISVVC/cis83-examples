#!/usr/bin/env python3

class Employee:

    def __init__(self,name):   # this is the constructor
        self.__fullname = name

    def __del__(self):        # this is a destructor
        print("The Employee destructor")
    
    def __repr__(self):
        return f'Employee()->{self.get_name()}'

    def get_name(self):
        return self.__fullname
    

class Hourly(Employee):

    def __init__(self,name,perhour):
        super().__init__(name)
        self.perhour = perhour

    def __del__(self):        # this is a destructor
        super().__del__()
        print("The Hourly destructor")
        print('_'*25)

    def weekly_pay(self,hours):
        return self.perhour * hours

    def __repr__(self):
        return f'Hourly()->{self.get_name()}'

class Salaried(Employee):

    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary

    def __del__(self):        # this is a destructor
        super().__del__()
        print("The Salaried destructor")
        print('_'*25)

    def __repr__(self):
        return f'Salaried()->{self.get_name()}'

    def weekly_pay(self,hours):
        return self.salary / 50

class Manager(Salaried):

    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus

    def __del__(self):        # this is a destructor
        super().__del__()
        print("The Manager destructor")
        print('_'*25)

    def __repr__(self):
        return f'Manager()->{self.get_name()}'

    def weekly_pay(self,hours):
        return super().weekly_pay(hours) + (hours-50) * self.bonus

def main():
   staff = []
   staff += [Hourly("Morgan, Harry",30)]
   staff += [Salaried("Lin, Salley", 52000)]
   staff += [Manager("Smith, Mary", 104000,50)]

   #staff += [Hourly("Morgan, Harry", 30)]
   #staff += [Salaried("Lin, Salley", 52000)]
   #staff += [Manager("Smith, Mary", 104000,50)]
      
   for e in staff:
      hours = int(input(f'Hours worked by {e.get_name()}: '))
      print(f'Weekly Pay: {e.weekly_pay(hours)}')

   print(staff)

if __name__ == "__main__":
    main()
