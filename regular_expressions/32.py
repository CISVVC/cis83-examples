#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-32.php
Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon.
"""

import re
text = 'Python Exercises, PHP exercises.'
print(re.sub("[ ,.]", ":", text, 2))

