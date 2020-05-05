#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-26.php
Write a Python program to match if two words from a list of words starting with letter 'P'.
"""

import re

# Sample strings.
words = ["Python PHP", "Java JavaScript", "c c++"]

for w in words:
        m = re.match("(P\w+)\W(P\w+)", w)
        # Check for success
        if m:
            print(m.groups())

