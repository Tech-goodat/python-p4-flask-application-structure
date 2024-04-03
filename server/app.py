from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>This is your homepage</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>your name is {username}</h1>'

if __name__=='__main__':
    app.run(port=5555)