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
[CN]把excel文件中的数据存入数据库的工作流程
[EN]the python work flow to push excel data in database table
"""

"""step0. import databse_engine, pandas, column_match
"""
import sqlite3
import pandas as pd
from HSH.DBA import colMatch

"""step1. connect to database
[EXAMPLE]
conn = psycopg2.connect(host = '127.0.0.1',  database = 'db_name', username = 'username', password = 'password')
c = conn.cursor()
"""
conn = sqlite3.connect(":memory:") ## example code
c = conn.cursor()
c.execute("CREATE TABLE employee (name TEXT, age INTEGER, height REAL, weight REAL, email TEXT, address TEXT)")

"""step2. load excel data, excel columns name, db_table columns name
[EXAMPLE]
dataframe = pd.read_excel('file_name.xlsx', 'spread_sheet_name')
xls_columns = dataframe.columns
xls_columns_dtype = dataframe.dtypes
db_columns = ... # it varies in different database systems
db_columns_dtype = ... # it varies in different database systems
"""
data = pd.read_excel("employee.xlsx", "Sheet1") ## example code
xls_columns = data.columns
xls_columns_dtypes = data.dtypes
db_columns = zip(*c.execute("PRAGMA table_info(employee)").fetchall() )[1]
db_columns_dtypes = zip(*c.execute("PRAGMA table_info(employee)").fetchall() )[2]

"""step3. match excel columns name to db_table columns name
[EXAMPLE]
col_map = colMatch.find_all_match(db_columns, xls_columns, tolerance = 4, verbal = False)
"""
col_map = colMatch.find_all_match(db_columns, xls_columns, tolerance = 4, verbal = False) ## example code

"""step5. insert data into database
[EXAMPLE]
for row in data:
    new_row = list()
    
    for item in row:
        new_row.append( processed(item) )
    
    c.execute('INSERT INTO ...')
"""
for ind in data.index: ## example code
    row = data.loc[ind,:] # 对于data中的每一行
    "generate new record to push"
    record = list()
    for db_column, db_columns_dtype in zip(db_columns, db_columns_dtypes):
        value = row[col_map[db_column]]
        if db_columns_dtype == "TEXT":
            value = str(value)
        elif db_columns_dtype == "INTEGER":
            value = int(value)
        elif db_columns_dtype == "REAL":
            value = float(value)
        record.append(value)
    
    "Insert into database"
    try: # remove try clause if you want to see error message
        c.execute("INSERT INTO employee VALUES (?,?,?,?,?,?)", record )
    except:
        pass

"""step6. browse data we pushed into the table
"""
for row in c.execute("SELECT * FROM employee").fetchall(): ## example code
    print row