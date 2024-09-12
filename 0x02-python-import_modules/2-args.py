#!/usr/bin/python3
import sys

argv = len(sys.argv) - 1

if argv == 1:
    print("{:d} argument:".format(argv))
elif argv == 0:
    print("{:d} arguments.".format(argv))
else:
    print("{:d} arguments:".format(argv))

i = 0
for arg in sys.argv:
    if i != 0:
        print("{:d}: {}".format(i, sys.argv[i]))
    i += 1
