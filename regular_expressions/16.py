#!/usr/bin/env python3

"""
https://www.w3resource.com/python-exercises/re/python-re-exercise-16.php
Write a Python program to remove leading zeros from an IP address.
"""
import re
ip = "216.08.094.196"
string = re.sub('\.[0]*', '.', ip)
print(string)
