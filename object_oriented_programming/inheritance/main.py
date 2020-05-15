#!/usr/bin/env python3

from hourly import Hourly
from salaried import Salaried
from manager import Manager

def main():
   staff = []
   staff += [Hourly("Morgan, Harry", 30)]
   staff += [Salaried("Lin, Salley", 52000)]
   staff += [Manager("Smith, Mary", 104000,50)]
      
   for e in staff:
      hours = int(input(f'Hours worked by " {e.get_name()}: '))
      print(f'Salary: e.weekly_pay(hours) << endl;
