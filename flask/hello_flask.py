from flask import Flask, render_template
from flask import request
from markupsafe import escape

app = Flask(__name__)

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/first-link')
def first_link():
    return render_template('contents/first-link.html')

@app.route('/second-link')
def second_link():
    return render_template('contents/second-link.html')

@app.route('/third-link')
def third_link():
    return render_template('contents/third-link.html')

@app.route('/fourth-link')
def fourth_link():
    return render_template('contents/fourth-link.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')

@app.route('/items', methods=['GET'])
def get_items():
    return {"item" : "Test Item"}

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

