#!/bin/usr/env python3
import re
import sys

regex = 'TASK \[.*\]'
for line in sys.stdin:
    line=line.rstrip('\n')
    x=re.search(regex,line)
    if x:
        print(x.group())