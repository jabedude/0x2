#!/usr/bin/env python

import sys

f = open(sys.argv[1], 'r')

for line in f:
    nums = [int(line.split()[0]), int(line.split()[1])]
    for x in range(1, int(float(nums[1])/nums[0]) + 1):
        print(x * nums[0])
