#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-27.php
Write a Python program to separate and print the numbers of a given string.
"""
import re
# Sample string.
text = "Ten 10, Twenty 20, Thirty 30"
result = re.split("\D+", text)
# Print results.
for element in result:
    print(element)
	
