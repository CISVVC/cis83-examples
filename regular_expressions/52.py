#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-52.php
Write a Python program that reads a given expression and evaluates it.

Terms and conditions:
The expression consists of numerical values, operators and parentheses, and the ends with '='.
The operators includes +, -, *, / where, represents, addition, subtraction, multiplication and division.
When two operators have the same precedence, they are applied to left to right.
You may assume that there is no division by zero.
All calculation is performed as integers, and after the decimal point should be truncated Length of the expression will not exceed 100.
-1 × 10 9 ≤ intermediate results of computation ≤ 10 9
"""
#https://bit.ly/2lxQysi
import re
print("Input number of data sets:")
class c(int):
    def __add__(self,n):
        return c(int(self)+int(n))
    def __sub__(self,n):
        return c(int(self)-int(n))
    def __mul__(self,n):
        return c(int(self)*int(n))
    def __truediv__(self,n):
        return c(int(int(self)/int(n)))

for _ in range(int(input())):
  print("Input an expression:")
  print(eval(re.sub(r'(\d+)',r'c(\1)',input()[:-1])))

