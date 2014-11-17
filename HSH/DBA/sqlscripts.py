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
经常我们需要写很多sql，而且每条sql中的参数都要经常更改
而我们每次通过注释，修改值的方式进行一次次的查询

如果有一段程序我们需要执行多次sql，并且把query的结果
当成参数传给下一个query，那么我们就需要一个标准化的流程
来做这样的事情。

请仔细阅读以下脚本，并将代码拷贝到你所需要用到的地方
"""

from __future__ import print_function
import sqlite3
from HSH.DBA.hsh_sqlite3 import iterC, prt_all
from prettytable import from_db_cursor

conn = sqlite3.connect("pdr - Copy.db")
c = conn.cursor()

def mk_query(i, parameters, prt_gen_all = 0):
    """从模板和参数表生成query，并输出结果
    第一步：
        定义所有的参数
    第二步：
        记录所有可能用到的模板
    第三部：
        执行查询，并按照三种模式中的一种，输出数据
    """
    table_name, device_id, DATE, DATE1, DATE2 = (parameters["table_name"],
                                                 parameters["device_id"],
                                                 parameters["DATE"],
                                                 parameters["DATE1"],
                                                 parameters["DATE2"])
    # 根据device_id获取全部信息
    query0 = \
    """
    SELECT * FROM %s WHERE device_id = '%s'
    """ % (table_name, device_id)
    
    # 查看所有的device_id
    query1 = \
    """
    SELECT DISTINCT device_id FROM %s
    """ % table_name    

    # 根据device_id查看某一天的power总和
    query2 = \
    """
    SELECT SUM(power) FROM 
    %s WHERE device_id = '%s' AND
    datetime_interval >= '%s 00:00:00' AND
    datetime_interval <= '%s 23:59:59'
    """ % (table_name, device_id, DATE, DATE)
    
    # 根据device_id查看某个时间区间的power总和
    query3 = \
    """
    SELECT SUM(power) FROM 
    %s WHERE device_id = '%s' AND
    datetime_interval >= '%s 00:00:00' AND
    datetime_interval <= '%s 23:59:59'
    """ % (table_name, device_id, DATE1, DATE2)
    
    c.execute(eval("query%s" % i))
    if prt_gen_all == 0: # 打印ascii二维表
        print(from_db_cursor(c))
    elif prt_gen_all == 1: # 生成器模式生成行
        return iterC(c)
    elif prt_gen_all == 2: # 返回整个二维表数据
        return c.fetchall()
    else:
        prt_all(c)

def main():
    parameters = {"table_name": "pdr_2014_treatment",
                  "device_id": "1008901017126564528128",
                  "DATE": "2014-01-01",
                  "DATE1": "2014-01-01",
                  "DATE2": "2014-08-31",}
    
    """ 主脚本 """
    for row in mk_query(1, parameters, 1):
        parameters["device_id"] = row[0]
        for row1 in mk_query(3, parameters, 1):
            print(row1[0])
    
if __name__ == "__main__":
    main()