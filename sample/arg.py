import sys

print(sys.argv)       # ['myscript.py', 'hello', 'world']
print(sys.argv[1:3])  # ['hello', 'world']
print(sys.argv[3])    # IndexError: list index out of range
print(len(sys.argv))   # 3
