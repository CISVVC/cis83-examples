#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-22.php
Write a Python program to find the occurrence and position of the substrings within a string.
"""
import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))

