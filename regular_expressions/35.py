#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-35.php
 Write a Python program to find all words which are at least 4 characters long in a string.    
"""

import re
text = 'The quick brown fox jumps over the lazy dog.'
print(re.findall(r"\b\w{4,}\b", text))

