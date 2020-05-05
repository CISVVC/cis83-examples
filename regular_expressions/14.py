#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-14.php
Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
"""

import re
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))

