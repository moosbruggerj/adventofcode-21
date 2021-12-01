#!/usr/bin/env python3

import sys
from math import *

if len(sys.argv) < 1:
    print("too few arguments", file=sys.stderr)
    print("usage: {} <input>".format(sys.argv[0]), file=sys.stderr)
    exit(1)

inputname = sys.argv[1]
#outputname = sys.argv[2]

countIncreased = 0
with open(inputname, "r") as inf:
    previous = int(next(inf))
    for line in inf:
        value = int(line)
        if value > previous:
            countIncreased += 1
        previous = value

    print(countIncreased)




