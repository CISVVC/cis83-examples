#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-36.php
Write a python program to convert camel case string to snake case string.
"""
def camel_to_snake(text):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

print(camel_to_snake('PythonExercises'))
