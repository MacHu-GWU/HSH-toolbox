import sqlite3
import pickle
import base64

# conn = sqlite3.connect(":memory:")
# c = conn.cursor()
# c.execute("create table test (obj TEXT) ")
# c.execute("insert into test values (?)", "a")
# print(c.execute("select * from test").fetchall())
# a = {1:"a", 2:"b"}
# c.execute("insert into test values (?)", pickle.dumps(a))
# print(c.execute("select * from test").fetchall())

a = {1:"a", 2:"b"}
b = pickle.dumps(a)
c = base64.b64encode(b)
print(type(b), type(c))
print(c)
print(pickle.loads(base64.b64decode(c)))
