#!/usr/bin/python3
import sys
sum = 0
if __name__ != "__main__":
    exit()
i = 0
for arg in sys.argv:
    if i != 0:
        sum += int(arg)
    i += 1
print("{:d}".format(sum))
