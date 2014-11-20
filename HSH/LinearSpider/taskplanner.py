##encoding=utf8

"""
第一层 - 入口表
CREATE TABLE layer1 (
self_id INTEGER,    # 用于节省空间
url TEXT UNIQUE,
ref TEXT,
PRIMARY KEY (self_id) );

CREATE TABLE layer2 (
id INTEGER,         # 外键
self_id INTEGER,    # 自己的
url TEXT UNIQUE,
ref TEXT
PRIMARY KEY (id, self_id) );

美国有51个州
state_id    url    ref
1
2
3
每个州有很多城市
state_id    city_id    url    ref
1            1
1            2
2            3
2            4
3            5
3            6
每个城市有很多个商店
city_id    url    ref
1
1
2
2
3
3
4
4
5
5
6
6
"""

from __future__ import print_function
import sqlite3

class TaskPlanner(object):
    def __init__(self, layer_number):
        