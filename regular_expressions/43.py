#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-43.php
Write a Python program to split a string at uppercase letters.
"""
import re
text = "PythonTutorialAndExercises"
print(re.findall('[A-Z][^A-Z]*', text))

