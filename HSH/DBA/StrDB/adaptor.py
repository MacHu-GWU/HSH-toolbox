##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-10-29             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""
"""

from __future__ import print_function
import pickle

def adapt_set(SET):
    """集合 -> 字符串 转换"""
    dtype = type(next(iter(SET)))
    if dtype == str:
        return "&".join(SET)
    elif dtype == int:
        return "&".join({int(i) for i in SET})
    elif dtype == float:
        return "&".join({float(i) for i in SET})
    else:
        raise Exception("error")
    
def convert_set(STRING):
    """字符串 -> 集合 转换
    强制转化成字符串的集合
    """
    return set(STRING.split('&'))

def adapt_list(LIST):
    """列表 -> 字符串 转换"""
    dtype = type(next(iter(LIST)))
    if dtype == str:
        return "&".join(LIST)
    elif dtype == int:
        return "&".join([int(i) for i in LIST])
    elif dtype == float:
        return "&".join([float(i) for i in LIST])
    else:
        raise Exception("Adaptor data type error")
    
def convert_list(STRING):
    """字符串 -> 列表 转换
    强制转化成字符串的列表
    """
    return STRING.split('&')

def adapt_any(OBJ):
    """任意对象字符串转换器"""
    return pickle.dumps(OBJ)

def convert_any(OBJ):
    """任意对象字符串转换器"""
    return pickle.loads(OBJ)

if __name__ == "__main__":
    import time
    import sqlite3
    def performance_test1():
        """对于内置数据类型list, set, tuple, dict, python都提供了内置repr函数使对象字符串化。从而我们可以
        从字符串中唯一的恢复原对象。
        
        虽然repr函数非常方便，但是性能上不一定是最佳的。
        例如说如果是一个字符串数组，我们可以用分隔符将其连起来。需要还原成列表时我们只需要将其分割开就好了。
        如果是一个整数数组，我们可以先转换类型，再用分隔符隔开。解码时反之亦然
        
        结论： 对于列表数据, join/split法要优于repr/eval
        """
    
        """字符串列表时，join/split法完胜
        """
        print("{:=^40}".format("字符串列表"))
        a = [str(i) for i in range(100000)]
         
        st = time.clock()
        s1 = "&".join(a)
        print("join法字符串化花了", time.clock()-st)
     
        st = time.clock()
        s2 = repr(a)
        print("repr法字符串化花了", time.clock()-st)
          
        st = time.clock()
        a1 = [char for char in s1.split("&")] # 分隔符的复杂程度对合并，拆分的速度影响不大
        print("split法拆分花了", time.clock()-st)
          
        st = time.clock()
        a2 = eval(s2)
        print("eval法拆分花了", time.clock()-st)
    
        """整数列表时，类到字符串的转化join法花费时间较长，字符串到类split法花费时间较短
        join/split法在查询量较大的数据库中，要远远优于repr/eval法
        """
        print("{:=^40}".format("整数列表"))
        a = [i for i in range(100000)]
         
        st = time.clock()
        s1 = "&".join([str(i) for i in a])
        print("join法字符串化花了", time.clock()-st)
     
        st = time.clock()
        s2 = repr(a)
        print("repr法字符串化花了", time.clock()-st)
          
        st = time.clock()
        a1 = [int(char) for char in s1.split("&")] # 分隔符的复杂程度对合并，拆分的速度影响不大
        print("split法拆分花了", time.clock()-st)
         
        st = time.clock()
        a2 = eval(s2)
        print("eval法拆分花了", time.clock()-st)
        
        """浮点数列表时，类到字符串的转化join法花费时间较长，字符串到类split法花费时间较短
        join/split法在查询量较大的数据库中，要远远优于repr/eval法
        """
        print("{:=^40}".format("浮点数列表"))
        a = [i*0.0001 for i in range(100000)]
        
        st = time.clock()
        s1 = "&".join([str(i) for i in a])
        print("join法字符串化花了", time.clock()-st)
    
        st = time.clock()
        s2 = repr(a)
        print("repr法字符串化花了", time.clock()-st)
         
        st = time.clock()
        a1 = [float(char) for char in s1.split("&")] # 分隔符的复杂程度对合并，拆分的速度影响不大
        print("split法拆分花了", time.clock()-st)
        
        st = time.clock()
        a2 = eval(s2)
        print("eval法拆分花了", time.clock()-st)
    
#     performance_test1()
    
    def performance_test2():
        """在adapt的对象是集合时，性能有大大的提升
        """
        """字符串集合时，join/split法完胜
        """
        print("{:=^40}".format("字符串集合"))
        a = {str(i) for i in range(10000)}
         
        st = time.clock()
        s1 = "&".join(a)
        print("join法字符串化花了", time.clock()-st)
     
        st = time.clock()
        s2 = repr(a)
        print("repr法字符串化花了", time.clock()-st)
          
        st = time.clock()
        a1 = {char for char in s1.split("&")} # 分隔符的复杂程度对合并，拆分的速度影响不大
        print("split法拆分花了", time.clock()-st)
          
        st = time.clock()
        a2 = eval(s2)
        print("eval法拆分花了", time.clock()-st)
    
        """整数集合时，类到字符串的转化join法花费时间较长，字符串到类split法花费时间较短
        join/split法在查询量较大的数据库中，要远远优于repr/eval法
        """
        print("{:=^40}".format("整数集合"))
        a = {str(i) for i in range(10000)}
         
        st = time.clock()
        s1 = "&".join({str(i) for i in a})
        print("join法字符串化花了", time.clock()-st)
     
        st = time.clock()
        s2 = repr(a)
        print("repr法字符串化花了", time.clock()-st)
          
        st = time.clock()
        a1 = {int(char) for char in s1.split("&")} # 分隔符的复杂程度对合并，拆分的速度影响不大
        print("split法拆分花了", time.clock()-st)
          
        st = time.clock()
        a2 = eval(s2)
        print("eval法拆分花了", time.clock()-st)
        
        """浮点数集合时，类到字符串的转化join法花费时间较长，字符串到类split法花费时间较短
        join/split法在查询量较大的数据库中，要远远优于repr/eval法
        """
        print("{:=^40}".format("浮点数集合"))
        a = {i*0.0001 for i in range(10000)}
         
        st = time.clock()
        s1 = "&".join({str(i) for i in a})
        print("join法字符串化花了", time.clock()-st)
     
        st = time.clock()
        s2 = repr(a)
        print("repr法字符串化花了", time.clock()-st)
          
        st = time.clock()
        a1 = {float(char) for char in s1.split("&")} # 分隔符的复杂程度对合并，拆分的速度影响不大
        print("split法拆分花了", time.clock()-st)
          
        st = time.clock()
        a2 = eval(s2)
        print("eval法拆分花了", time.clock()-st)
        
#     performance_test2()
    
    def performance_test3():
        import pickle
        print("{:=^40}".format("pickle完胜"))
        a = {str(i) for i in range(10000)}
         
        st = time.clock()
        s1 = "&".join(a)
        print("join法字符串化花了", time.clock()-st)
     
        st = time.clock()
        s2 = repr(a)
        print("repr法字符串化花了", time.clock()-st)
        
        st = time.clock()
        s3 = pickle.dumps(a)
        print("pickle法字符串化花了", time.clock()-st)
    
        st = time.clock()
        a1 = {char for char in s1.split("&")} # 分隔符的复杂程度对合并，拆分的速度影响不大
        print("split法拆分花了", time.clock()-st)
          
        st = time.clock()
        a2 = eval(s2)
        print("eval法拆分花了", time.clock()-st)
        
        st = time.clock()
        a3 = pickle.loads(s3)
        print("pickle法拆分花了", time.clock()-st)
        
#     performance_test3()
    
    def unit_test1():
        sqlite3.register_adapter(set, adapt_set) # 注册转换器
        sqlite3.register_converter("STRSET", convert_set) # 定义新的数据类型
        conn = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
        c = conn.cursor()
        c.execute("CREATE TABLE test (id_set STRSET)")
        c.execute("INSERT INTO test (id_set) VALUES (?)", ( {"a01", "a02", "a03"},) )
        print(c.execute("SELECT * FROM test").fetchall())
        
#     unit_test1()

    def unit_test2():
        sqlite3.register_adapter(dict, adapt_any) # 注册转换器
        sqlite3.register_converter("STRSET", convert_any) # 定义新的数据类型
        conn = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
        c = conn.cursor()
        c.execute("CREATE TABLE test (id_set STRSET)")
        c.execute("INSERT INTO test (id_set) VALUES (?)", ( {1:"a", 2:"b", 3:"c"},) )
        print(c.execute("SELECT * FROM test").fetchall())
        
    unit_test2()