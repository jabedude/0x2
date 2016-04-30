#!/usr/bin/env python

import os
import datetime
import sys
def modification_date(filename):
    m = os.path.getmtime(filename)
    a = os.path.getatime(filename)
    c = os.path.getatime(filename)

    print datetime.datetime.fromtimestamp(m)
    print datetime.datetime.fromtimestamp(a)
    print datetime.datetime.fromtimestamp(c)

modification_date(sys.argv[1])
