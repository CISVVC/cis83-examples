#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-46.php
Write a Python program to find all adverbs and their positions in a given sentence.
"""

import re
text = "Clearly, he has no excuse for such behavior."
for m in re.finditer(r"\w+ly", text):
    print('%d-%d: %s' % (m.start(), m.end(), m.group(0)))

