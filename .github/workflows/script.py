import sys

try:
    number = int(sys.argv[1])
    print("Result:", number + 10)
except (IndexError, ValueError):
    print("Please pass a valid number as an argument.")
