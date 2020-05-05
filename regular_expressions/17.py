#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-17.php
Write a Python program to check for a number at the end of a string.
"""

import re
def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False

print(end_num('abcdef'))
print(end_num('abcdef6'))

