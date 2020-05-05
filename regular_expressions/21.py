#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-21.php
Write a Python program to find the substrings within a string.

Note: There are two instances of exercises in the input string.
"""

import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)

