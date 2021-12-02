#!/usr/bin/env python3

import sys
from math import *

if len(sys.argv) < 1:
    print("too few arguments", file=sys.stderr)
    print("usage: {} <input>".format(sys.argv[0]), file=sys.stderr)
    exit(1)

inputname = sys.argv[1]
#outputname = sys.argv[2]

horizontal = 0
depth = 0

with open(inputname, "r") as inf:
    for line in inf:
        instruction = line.split(" ")
        
        amount = int(instruction[1])
        if instruction[0] == "forward":
            horizontal += amount
        elif instruction[0] == "up":
            depth -= amount
        elif instruction[0] == "down":
            depth += amount

    print(horizontal*depth)




