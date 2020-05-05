#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-23.php
Write a Python program to replace whitespaces with an underscore and vice versa.
"""
import re
text = 'Python Exercises'
text =text.replace (" ", "_")
print(text)
text =text.replace ("_", " ")
print(text)

