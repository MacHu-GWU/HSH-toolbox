##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-22

from __future__ import print_function
from HSH.Data.pk import load_pk, dump_pk

def unit_test():
    obj = {1: ["a1", "a2"], 2: ["b1", "b2"]}    # 初始化数据
    dump_pk(obj, "obj.p", 2, replace = True)  # 测试 dump_pk
    print(load_pk("obj.p") )              # 测试 load_pk                           
        
if __name__ == "__main__":
    unit_test() # 2014-10-11 python2.7.6 和 3.3.3 测试通过