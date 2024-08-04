import sqlite3

from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response

app = Flask(__name__)

def get_db():
    # g はグローバル情報を保持
    # _database という名前を付けてアクセスする。
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('test_sqlite.db')
    return db

# リクエストごとにコールされる
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    # 保持していた _database を取得する
    if db is not None:
        db.close()
    # _database は一度のセッションの間しか保持されないらしい

@app.route('/employee', methods=['POST', 'PUT', 'DELETE'])
@app.route('/employee/<name>', methods=['GET'])
def employee(name=None):
    db = get_db()
    curs = db.cursor()

    # 通常はテーブル生成はリクエストのタイミングではなく、
    # アプリケーションの起動のタイミングで行っておく
    curs.execute(
        'CREATE TABLE IF NOT EXISTS persons('
        'id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
    )
    db.commit()

    name = request.values.get('name', name)
    if request.method == 'GET':
        curs.execute('SELECT * FROM persons WHERE name = "{}"'.format(name))
        person = curs.fetchone()
        if not person:
            return "No", 404
        user_id, name = person
        return '{}:{}'.format(user_id, name), 200

    # POST は追加
    if request.method == 'POST':
        curs.execute('INSERT INTO persons(name) values("{}")'.format(name))
        db.commit()
        return 'created {}'.format(name), 201

    # PUT は更新
    if request.method == 'PUT':
        # new_nameは必ず指定されるべきもの。あえてget()は使わない。
        new_name = request.values['new_name']
        curs.execute('UPDATE persons set name = "{}" WHERE name = "{}"'.format(
            new_name, name
        ))
        db.commit()
        return 'update {}: {}'.format(name, new_name), 200

    if request.method == 'DELETE':
        curs.execute('DELETE from persons WHERE name = "{}"'.format(name))
        db.commit()
        return 'deleted {}'.format(name), 200


@app.route('/')
def hello_world():
    return 'top'

@app.route('/hello')
@app.route('/hello/<username>')
def hello_world_username(username=None):
    return 'hello world {}'.format(username)

@app.route('/hello_template')
@app.route('/hello_template/<username>')
def hello_world_template(username=None):
    return render_template('hello.html', username=username)

@app.route('/post', methods=['POST', 'PUT', 'DELETE'])
def show_post():
    # flaskが request に値を設定してくれている
    return str(type(request.values))
    # return str(request.values['username'])

def main():
    app.debug = True
    app.run()
    # app.run(host='127.0.0.1', port=5000)

if __name__ == '__main__':
    main()
