#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-1.php
 Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
"""
import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))
