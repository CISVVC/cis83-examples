#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-53.php
Write a Python program to remove lowercase substrings from a given string.
"""
import re
str1 = 'KDeoALOklOOHserfLoAJSIskdsf'
print("Original string:")
print(str1)
print("After removing lowercase letters, above string becomes:")
remove_lower = lambda text: re.sub('[a-z]', '', text)
result =  remove_lower(str1)
print(result)

