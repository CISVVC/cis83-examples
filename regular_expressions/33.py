#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-33.php
Write a Python program to find all five characters long word in a string.
"""
import re
text = 'The quick brown fox jumps over the lazy dog.'
print(re.findall(r"\b\w{5}\b", text))

