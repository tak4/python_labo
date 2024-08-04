from flask import Flask, render_template
from flask import request
import json #必ず必要

app = Flask(__name__)

# アプリ起動
if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')

# JSONをレスポンスする
@app.route('/case1', methods=['GET'])
def get_response():
    # レスポンス用のJSON読み込み
    with open("json/response_case1.json" , "r") as jf:
        f_json = json.load(jf)
    return f_json

# リクエスト変数を受ける
@app.route("/requestval", methods=['GET'])
def get_requestval():
    # リクエスト変数を受け取る
    name = request.args.get("name")
    age = request.args.get("age")

    # リクエスト変数を使って処理を行う
    return f'{{"name": {name}, "age": {age}}}'
