##encoding=utf8
##version =py27
##author  =sanhe
##date    =2014-09-12

from __future__ import print_function
from HSH.DBA.hsh_sqlite3 import Database_schema, iterC, prt_all, stable_insertmany
import sqlite3
import datetime

def unit_test1():
    try:
        conn = sqlite3.connect("employee.db")
        c = conn.cursor()
        c.execute("CREATE TABLE people (id INTEGER PRIMARY KEY NOT NULL, name TEXT, enroll_date DATE);")
        c.execute("CREATE TABLE salary (id INTEGER PRIMARY KEY NOT NULL, hour_rate INTEGER);")
        c.execute("INSERT INTO people (id, name, enroll_date) VALUES (?, ?, ?)", (1, "Jack", datetime.date(2014,8,15) ) )
        c.execute("INSERT INTO salary (id, hour_rate) VALUES (?, ?)", (1, 25) )
        conn.commit()
    except:
        print("""Something Wrong, please delete 'records.db' then proceed""")

    db_schema = Database_schema("employee.db")
    print(db_schema)
    print(db_schema.people)
    print(db_schema.salary)

def unit_test2():
    """测试stable_insertmany的功能
    """
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("CREATE TABLE test (id INTEGER PRIMARY KEY NOT NULL, number INTEGER)")
    records = [(1, 10), (3, 10), (5, 10)] # insert some records at begin
    c.executemany("INSERT INTO test VALUES (?, ?)", records)
    
    records = [(2, 10), (3, 10), (4, 10)]
    stable_insertmany(conn, c, "INSERT INTO test VALUES (?, ?)", records)
    c.execute("SELECT * FROM test")
    prt_all(c)
    
if __name__ == "__main__":
    unit_test1()
    unit_test2()
    