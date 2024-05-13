#!/bin/usr/python

import sys 

code = sys.argv[1]

country = {'India':'INR',
           'Russia': 'RU',
           'Qatar' : 'QR',
           'China' : 'Ch',
           'Pakistan': 'PK',
           }
if code in country:
    print(f' Country code of', sys.argv[1] , f'is' , country[code])
else:
   print("enter correct data")