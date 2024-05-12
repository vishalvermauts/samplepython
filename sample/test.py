#!/bin/usr/env python3

import re
import sys

regex=input("Enter a regex expression: ")
#sentence = input("Enter a replacement: ")
print("Enter some more Lines: ")
for line in sys.stdin:
    line=line.rstrip("\n")
    x=re.findall(regex,line)
    if x:
        print("Replaced sentence is ", x)
