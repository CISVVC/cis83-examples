#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-38.php
Write a Python program to extract values between quotation marks of a string.
"""
import re
text1 = '"Python", "PHP", "Java"'
print(re.findall(r'"(.*?)"', text1))

