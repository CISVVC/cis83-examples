#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-37.php
Write a python program to convert snake case string to camel case string.
"""
def snake_to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snake_to_camel('python_exercises'))

