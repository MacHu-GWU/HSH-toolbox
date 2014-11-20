##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-10-12

from __future__ import print_function
from HSH.OS import *

def unit_test():
    print(string_SizeInBytes(4342898583164) )
    print(getdirsize(r"C:\HSH\Workspace\py27_projects\HSH-toolbox") )
    print(get_dirinfo(r"C:\HSH\Workspace\py27_projects\HSH-toolbox"))
#     find_bigdir(r"C:\HSH\Workspace\py27_projects\HSH-toolbox", 1000)
#     find_bigfile(r"C:\HSH\Workspace\py27_projects\HSH-toolbox", 1000)

if __name__ == "__main__":
    unit_test()