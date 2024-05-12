#!/bin/usr/env python3

import sys



name = input("Enter Your Name: ")
grade = int(sys.argv[1])

if grade > 85:
    grade='HD'
elif grade>=85:
   grade='A'
elif grade>=75:
    grade='B'
elif grade>=65:
    grade='c'
else:
    grade='Fail'
print(f'{name} your grade is {grade}')