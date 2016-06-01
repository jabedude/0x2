#!/usr/bin/env python

def stack_string(str):
    reverse = str[::-1]
    hex_string = reverse.encode('hex')
    

print stack_string('/sbin///iptables')
