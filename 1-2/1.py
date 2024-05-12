#!/bin/usr/env python3

import sys



name = input("Enter Your Name: ")
grade = int(sys.argv[1])

if grade > 85:
    print("HD")
elif grade>=85:
    print("A")
elif grade>=75:
    print("B")
elif grade>=65:
    print("c")
else:
    print("Fail")