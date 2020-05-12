#!/usr/bin/env python3
class Employee:
    def __init__(self,name="No Name"):
        self.name = name 

    def set_name(self,name):
        self.name = name 

    def get_name(self):
        return self.name

    def weekly_pay(self,hours_worked):
        return 0

    def __repr__(self):
        return f'<Employee({self.name})>'

if __name__ == '__main__':
    e = Employee("Fred")
    print(e)
