#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-47.php


Write a Python program to split a string with multiple delimiters.

Note : A delimiter is a sequence of one or more characters used to specify the boundary between separate, independent regions in plain text or other data streams. An example of a delimiter is the comma character, which acts as a field delimiter in a sequence of comma-separated values.
"""
import re
text = 'The quick brown\nfox jumps*over the lazy dog.'
print(re.split('; |, |\*|\n',text))

