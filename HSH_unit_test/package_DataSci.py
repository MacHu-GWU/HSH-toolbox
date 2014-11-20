##encoding=utf8

from __future__ import print_function
try: # 可以一次性全部倒入
    from HSH.DataSci import *
except: # 也可以单独导入
    from HSH.DataSci import knn
    from HSH.DataSci import linreg
    from HSH.DataSci import preprocess
    from HSH.DataSci import psmatcher
    from HSH.DataSci import stat
    
def test_import():
    print(knn.dist)
    print(knn.knn_classify)
    print(knn.knn_find)
    print(linreg.linreg_predict)
    print(linreg.linreg_coef)
    print(linreg.glance_2d)
    
test_import()