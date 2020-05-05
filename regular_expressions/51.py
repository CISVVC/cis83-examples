#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-51.php
Write a Python program to insert spaces between words starting with capital letters.
"""
import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces("Python"))
print(capital_words_spaces("PythonExercises"))
print(capital_words_spaces("PythonExercisesPracticeSolution"))

