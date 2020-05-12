#!/usr/bin/env python3
from employee import Employee

class Salaried(Employee):
    def __init__(self,name="No Name",salary=0):
        Employee.__init__(self,name)
        self.salary = salary

    def weekly_pay(self,hours_worked):
       WEEKS_PER_YEAR = 52
       return self.salary / WEEKS_PER_YEAR

    def __repr__(self):
        return f'<Salaried({self.name})>'

if __name__ == '__main__':
    e = Salaried("Fred",48000.0)
    print(e)
    print(f'{e.weekly_pay(80):.2f}')


