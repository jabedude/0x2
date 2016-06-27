#!/usr/bin/env python

import httplib

cl = httplib.HTTPConnection('www.google.com')
cl.request('GET', '/')

resp = cl.getresponse()
print resp.status , resp.reason
