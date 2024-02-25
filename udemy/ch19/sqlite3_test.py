import sqlite3

conn = sqlite3.connect("datafile.db")
cursor = conn.cursor()
# cursor.execute(
#     """create table people (id integer primary key, name text, count integer)""")

# todo: insert
# cursor.execute(
#     """insert into people (name, count) values (?, ?)""", ("bob", 25))

# cursor.execute(
#     """insert into people (name, count) values (:username, :usercount)""", {"username": "duncan", "usercount": 25})

# todo: update
# cursor.execute("""update people set count = :usercount where name = :username""", {
#                "username": "bob", "usercount": 18})

# todo: delete
# cursor.execute("""Delete from people where name ='bob'""")

result = cursor.execute("select * from people")
print(result.fetchall())

conn.commit()
conn.close()
