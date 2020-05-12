#!/usr/bin/env python3
from employee import Employee
class Hourly(Employee):
    def __init__(self,name="No Name",salary=15.0):
        Employee.__init__(self,name)
        self.wage = wage

    def set_name(self,name):
        self.name = name 

    def get_name(self):
        return self.name

    def weekly_pay(self,hours_worked):
       pay = hours_worked * self.wage
       if hours_worked > 40:
          pay = pay + ((hours_worked - 40) * 0.5) * self.wage
       return pay

    def __repr__(self):
        return f'<Hourly({self.name})>'

if __name__ == '__main__':
    e = Hourly("Fred",20.0)
    print(e)
    print(e.weekly_pay(80))
