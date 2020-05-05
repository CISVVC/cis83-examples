#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-29.php
Write a Python program to separate and print the numbers and their position of a given string.
"""
import re
# Input.
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position:", m.start())
