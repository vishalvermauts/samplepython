#!/usr/bin/env python3
import sys
import re

regex = input('Enter a Regular Express: ')
print("Regex: ", regex)

print('Enter Some Lines: ')
for line in sys.stdin:
    line=line.strip("\n")
    
    x = re.findall(regex,line)
    if x:
        print("Line: ", line)
        print("Matched Line: ",x)