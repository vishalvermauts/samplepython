#!/bin/usr/python
import sys

mood = sys.argv[1]

if (mood == 'India'):
    print("IN")
elif (mood == 'China'): 
    print("CN")
elif (mood == 'Russia'):
    print('RU')
elif (mood == 'IRAN'):
    print('IR')
elif (mood == 'Qatar'):
    print("QR")
else:
    print("Enter correct data")

