#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-10.php
Write a Python program that matches a word at the beginning of a string.
"""

import re
def text_match(text):
        patterns = '^\w+'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match(" The quick brown fox jumps over the lazy dog."))

