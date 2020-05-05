#!/usr/bin/env python3
"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-4.php
Write a Python program that matches a string that has an a followed by zero or one 'b'.
"""
import re
def text_match(text):
        patterns = 'ab?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ab"))
print(text_match("abc"))
print(text_match("abbc"))
print(text_match("aabbc"))

