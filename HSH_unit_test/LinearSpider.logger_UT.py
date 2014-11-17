##encoding=utf8
##version =py27, py34
##author  =sanhe
##date    =2014-09-11

from __future__ import print_function
from HSH.LinearSpider.logger import Log

def unit_test():
    log = Log()
    log.write("request denied", ("www.python.org", 5))
    log.clear_all()
    
if __name__ == "__main__":
    unit_test()