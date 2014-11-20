##encoding=utf8

from __future__ import print_function
from HSH.Data import *
import os

class Excel2db_unittest():
    @staticmethod
    def excel2sqlite():
        excel2sqlite(r"dataset\wc3_demo_db.xlsx")

class Js_unittest():
    @staticmethod
    def everything():
        """test three main function in js:
        load_js, dump_js, prt_js
        """
        print("{:=^100}".format("json_everything"))
        data = {1: ["a1", "a2"], 2: ["b1", "b2"]}   # 初始化数据
        dump_js(data, "data.json", replace = True)  # 测试 dump_js
        print ( load_js("data.json") )              # 测试 load_js
        prt_js(data)                                # 测试 prt_js
        os.remove("data.json")                      # 清除掉残留文件
      
        
class Pk_unittest():
    @staticmethod
    def everything():
        """test two main function in js:
        load_pk, dump_pk
        """
        print("{:=^100}".format("pickle_everything"))
        obj = {1: ["a1", "a2"], 2: ["b1", "b2"]}    # 初始化数据
        dump_pk(obj, "obj.p", 2, replace = True)    # 测试 dump_pk
        print(load_pk("obj.p") )                    # 测试 load_pk
        os.remove("obj.p")                          # 清除掉残留文件
        
if __name__ == "__main__":
    Excel2db_unittest.excel2sqlite()
    Js_unittest.everything()
    Pk_unittest.everything()