#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-19.php
Write a Python program to search some literals strings in a string.
"""
import re
patterns = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text),)
    if re.search(pattern,  text):
        print('Matched!')
    else:
        print('Not Matched!')
		
