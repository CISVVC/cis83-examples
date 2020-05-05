#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-40.php
Write a Python program to remove all whitespaces from a string.
"""

import re
text1 = ' Python    Exercises '
print("Original string:",text1)
print("Without extra spaces:",re.sub(r'\s+', '',text1))

