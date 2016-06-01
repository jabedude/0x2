#!/usr/bin/env python

def stack_string(str):
    reverse = str[::-1]
    hex_string = reverse.encode('hex')
    if len(hex_string) % 8 != 0:
        print "String literal not able to be aligned by 4-bytes"
        pass
    for i in range(0, len(hex_string), 8):
        print '0x' + hex_string[0+i:8+i]


stack_string("/sbin///iptables")
