#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-39.php
Write a Python program to remove multiple spaces in a string.
"""

import re
text1 = 'Python      Exercises'
print("Original string:",text1)
print("Without extra spaces:",re.sub(' +',' ',text1))

