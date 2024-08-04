# 135. SQLite

import sqlite3

# データベースファイルを作成する方法
conn = sqlite3.connect('test.db')
# データベースをメモリ上で処理する方法
# conn = sqlite3.connect(':memory:')


# カーソル作成
curs = conn.cursor()

curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
)
conn.commit()

curs.execute(
    'INSERT INTO persons(name) values("Alice")'
)
conn.commit()

curs.execute(
    'INSERT INTO persons(name) values("Bob")'
)
conn.commit()

curs.execute(
    'INSERT INTO persons(name) values("Charlie")'
)
conn.commit()

curs.execute(
    'UPDATE persons set name = "Charles" WHERE name = "Charlie"'
)
conn.commit()

curs.execute(
    'DELETE FROM persons WHERE name = "Charles"'
)
conn.commit()

curs.execute(
    'SELECT * FROM persons'
)
print(curs.fetchall())

curs.close()
conn.close()
