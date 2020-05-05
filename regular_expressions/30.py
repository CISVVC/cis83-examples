#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-30.php
Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.
"""

import re
street = '21 Ramkrishna Road'
print(re.sub('Road$', 'Rd.', street))

