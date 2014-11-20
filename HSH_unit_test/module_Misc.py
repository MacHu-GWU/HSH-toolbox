##encoding=utf8

from __future__ import print_function
from HSH.Misc import *

def add2(a, b):
    return a + b

a, b = 1, "2"
try:
    tryit(3, add2, a, b)
except Exception as e:
    print(e)