##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-10-12

from __future__ import print_function
from HSH.OS.smtf import getdirsize, string_SizeInBytes, get_dirinfo
import os

def unit_test():
    print(getdirsize(os.getcwd() ) )
    print(string_SizeInBytes(4342898583164) )
#     print(getdirsize(r"smtf.py") )
    print(get_dirinfo(os.getcwd() ) )
    
if __name__ == "__main__":
    unit_test()