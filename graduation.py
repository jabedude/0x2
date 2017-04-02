#!/usr/bin/env python
from datetime import date

t = date(2018,3,24) -date.today()

print('{} days until graduation!'.format(t.days))
