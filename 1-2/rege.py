#!/bin/usr/env python3

import re

string1='My Name is Vishal Verma'

name=input("Enter any regex expression: ")

print(re.match(name,string1))
print(re.findall(name,string1))
print(re.search(name,string1))

replacement=input("Enter replacement text: ")

print(re.sub(name,replacement,string1))