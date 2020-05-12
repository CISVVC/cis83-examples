#!/usr/bin/env python3
from salaried import Salaried

class Manager(Salaried):
    def __init__(self,name="No Name",salary=0,bonus=0):
        Salaried.__init__(self,name,salary)
        self.bonus = bonus

    def weekly_pay(self,hours):
       return Salaried.weekly_pay(self,hours) + self.bonus;

    def __repr__(self):
        return f'<Manager({self.name})>'

if __name__ == '__main__':
    e = Manager("Fred",48000.0,1000)
    print(e)
    print(f'{e.weekly_pay(80):.2f}')
