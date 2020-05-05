#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-20.php
Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs.
"""
import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % \
    (match.re.pattern, match.string, s, e))
	
