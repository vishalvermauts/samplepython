import sys

# Read a line of input from the user
print("Enter your name:")
name = sys.stdin.readline().strip()  # Read a line from stdin and remove whitespace

# Display the input
print("Hello,", name)
