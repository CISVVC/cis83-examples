#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-28.php
Write a Python program to find all words starting with 'a' or 'e' in a given string.
https://www.w3resource.com/python-exercises/re/python-re-exercise-28.php
"""

import re
# Input.
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
#find all the words starting with 'a' or 'e'
list = re.findall("[ae]\w+", text)
# Print result.
print(list)

