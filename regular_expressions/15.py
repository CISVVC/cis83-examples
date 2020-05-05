#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-15.php
Write a Python program where a string will start with a specific number.
"""

import re
def match_num(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False
print(match_num('5-2345861'))
print(match_num('6-2345861'))

