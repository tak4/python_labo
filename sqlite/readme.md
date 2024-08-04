# SQLite

## 公式サイト
https://www.sqlite.org/index.html


## Console

コンソール起動  
`sqlite3`
`sqlite3 [*.db]`

コンソール操作例  

```
$ sqlite3
SQLite version 3.37.2 2022-01-06 13:25:41
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING);
sqlite> INSERT INTO persons(name) values("Alice");
sqlite> INSERT INTO persons(name) values("Bob");
sqlite> INSERT INTO persons(name) values("Charlie");
sqlite> UPDATE persons set name = "Charles" WHERE name = "Charlie";
sqlite> DELETE FROM persons WHERE name = "Charles";
sqlite> .tables
persons
sqlite> SELECT * FROM persons;
1|Alice
2|Bob
sqlite> .save test.db
sqlite> .exit
```

```
$ sqlite3 test.db
SQLite version 3.37.2 2022-01-06 13:25:41
Enter ".help" for usage hints.
sqlite> .tables
persons
sqlite> SELECT * FROM persons;
1|Alice
2|Bob
sqlite> .exit
```



