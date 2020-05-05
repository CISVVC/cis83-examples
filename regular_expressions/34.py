#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-34.php
Write a Python program to find all three, four, five characters long words in a string.
"""
import re
text = 'The quick brown fox jumps over the lazy dog.'
print(re.findall(r"\b\w{3,5}\b", text))

