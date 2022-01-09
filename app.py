from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'


@app.route('/html')
def show():
    return '<h1>Hello zhuzhu!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/user/<name>')
def user_page(name):
    return 'User %s' % name


@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='wemo'))
    print(url_for('test_url_for'))

    print(url_for('test_url_for', num=2))  # 输出: /test?num=2

    return 'Test page'

