##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-10-13

from __future__ import print_function
from HSH.DataSci.stat import find_outlier, clear_outlier_onetime, clear_outlier_literally
import numpy as np

def unit_test1():
    data = np.array([3, 2.9, 3.1, 4.2, 2.7, 3.5, 6.8, 12.7])
    print(clear_outlier_onetime(data) )
    print(clear_outlier_literally(data) )
    print(find_outlier(data) )
    
if __name__ == "__main__":
    unit_test1()