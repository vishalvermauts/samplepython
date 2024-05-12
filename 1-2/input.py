import sys


name=input("Enter your Name: ")
print(name)


fname=sys.argv[1]
lname=sys.argv[2]
mname=sys.argv[3]

print(f'{fname}, {mname}- {lname}')


