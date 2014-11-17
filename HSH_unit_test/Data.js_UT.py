##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-22

from __future__ import print_function
from HSH.Data.js import load_js, dump_js, prt_js

def unit_test():
    data = {1: ["a1", "a2"], 2: ["b1", "b2"]}   # 初始化数据
    dump_js(data, "data.json", replace = True)  # 测试 dump_js
    print ( load_js("data.json") )              # 测试 load_js
    prt_js(data)                                # 测试 prt_js
        
if __name__ == "__main__":
    unit_test() # 2014-10-11 python2.7.6 和 3.3.3 测试通过