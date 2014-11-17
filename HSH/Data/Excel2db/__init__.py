##################################
#encoding=utf8                   #
#version =py27, py33             #
#author  =sanhe                  #
#date    =2014-10-31             #
#                                #
#    (\ (\                       #
#    ( -.-)o    I am a Rabbit!   #
#    o_(")(")                    #
#                                #
##################################

"""
情况1
    数据库里没有表格，需要根据excel表格建立数据库
        --- pandas.to_sql模块
        
情况2
    数据库里有表格，表格格式和excel一样，批量的导入
    数据 
        --- 许多数据库软件自带这类的工具
    
情况3
    数据库里有表格，表格格式和excel不同，但是数据
    表中的列一定能在excel表中找到。 
        --- 需要建立一种map关系
"""

from excel_to_db import xlsx_to_sqlite