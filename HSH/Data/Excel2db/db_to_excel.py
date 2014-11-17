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
本脚本用于从excel文件生成一个database
    每个excel spreadsheet是一个tabel
    每个spreadsheet的column是一个table的column

引擎会按照下表进行数据格式的转换
    int to int, float to float, str to str
    int like str to int, float like str to float
    datetime to datetime, date to datetime
"""

from __future__ import print_function
from sqlalchemy import create_engine
import pandas as pd
import sqlite3
import os

def sqlite_to_xlsx(excel_name):
    """创建一个与excel文件同名的
    只支持xlsx2013以上的版本
    """