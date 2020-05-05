#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-41.php
Write a Python program to remove everything except alphanumeric characters from a string.
"""
import re
text1 = '**//Python Exercises// - 12. '
pattern = re.compile('[\W_]+')
print(pattern.sub('', text1))

