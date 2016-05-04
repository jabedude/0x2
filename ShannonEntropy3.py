#!/usr/bin/env python3
import collections
import sys
import math

def ShannonEntropy(inputString):
    total = 0.0
    length = float(len(inputString))
    for char in inputString:
        charFreq = inputString.count(char) / length
        total += (charFreq * math.log2(charFreq)) 
    #print( total )
for i in collections.Counter(sys.argv[1]).values():
    print( -sum( i/len(sys.argv[1]) * math.log2( i/len(sys.argv[1]) ) ) )
ShannonEntropy(sys.argv[1])

