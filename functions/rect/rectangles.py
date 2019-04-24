#!/usr/bin/env python3

def get_dimensions():
   length = float(input("Enter the length:"))
   width = float(input("Enter the width:"))
   return (length,width)

def calc_perimeter(dimensions):
   return dimensions[0] * 2 + dimensions[1] * 2

def calc_area(length,width):
   return length * width

def display_perimeter(length,width):
   d = (length,width)
   print("The perimeter for a rectangle that has length = {} and a width = {} is: {}"
          .format(length,width,calc_perimeter(  d )))

def display_area(length,width):
   print("The area for a rectangle that has length = {} and a width = {} is: {}"
          .format(length,width,calc_area(length,width)))

def start():
   dimensions = get_dimensions()
   display_perimeter(dimensions[0],dimensions[1])
   display_area(dimensions[0],dimensions[1])

if __name__ == "__main__":
   start()

