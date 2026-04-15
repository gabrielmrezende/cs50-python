import sys

if len(sys.argv) < 2:
    sys.exit("Too feew arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
print("Hello, my name is", sys.argv[1])
