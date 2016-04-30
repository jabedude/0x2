#!/usr/bin/env python
import sys
import math

def ShannonEntropy(inputString):
    total = 0
    length = float(len(inputString))
    for char in inputString:
        charFreq = inputString.count(char) / length
        print charFreq
        total += charFreq * (math.log(charFreq)/math.log(2))
    #print -1 * total

ShannonEntropy(sys.argv[1])
