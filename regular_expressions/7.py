#!/usr/bin/env python3
"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-7.php
Write a Python program to find sequences of lowercase letters joined with a underscore.
"""

import re
def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))

