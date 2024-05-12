#!/bin/usr/ env python3
import sys
import re


regex = input("Enter a regular express: ")
replacement = input("Enter a replacement: ")
#print("%s %f" %(regex,replacement) )
print("Enter some line: ")
for line in sys.stdin:
    line=line.rstrip("\n")
    x = re.sub(regex,replacement,line)
    print("Line with replacement : ", x)

