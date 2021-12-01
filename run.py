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
    window = [int(next(inf)), int(next(inf)), int(next(inf))]
    for line in inf:
        value = int(line)
        if window[1] + window[2] + value > sum(window):
            countIncreased += 1
        window = window[1:] + [value]

    print(countIncreased)




