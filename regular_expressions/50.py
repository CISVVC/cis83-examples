#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-50.php
Write a Python program to remove the parenthesis area in a string.
"""

import re
items = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
for item in items:
    print(re.sub(r" ?\([^)]+\)", "", item))

