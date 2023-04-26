from bottle import route, run, template
from bottle import get, post, request # or route

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/hello')
def hello():
    return "Hello World_2!"

@route('/hello/toplama')
def toplma():
    a=int(input("input1: "))
    b=int(input("input2: "))
    c=a+b
    return f'{a}+{b}={c}'

@get('/login') # or @route('/login')
def login():
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Login Form</title>
            <style>
            body {
                background-color: turquoise;
            }
            form {
                width: 300px;
                margin: 0 auto;
                padding: 20px;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
            }
            label, input[type="text"], input[type="password"], input[type="submit"] {
                display: block;
                width: 100%;
                margin-bottom: 10px;
            }
            label {
                font-weight: bold;
            }
            input[type="text"], input[type="password"] {
                padding: 10px;
                border-radius: 5px;
                border: none;
                box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.1);
            }
            input[type="submit"] {
                padding: 10px;
                background-color: turquoise;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            </style>
        </head>
        <body>
            <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
        </body>
        </html>

    '''

@get('/login2') # or @route('/login')
def login2():
    return '''
        <form action="/login2" method="post">
            Username: <input name="username2" type="text" />
            Password: <input name="password2" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''



def check_login(username,password):
    if username=="ozd" and password=="123":
        return True
    else:
        return False

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

@post('/login2') # or @route('/login', method='POST')
def do_login2():
    username = request.forms.get('username2')
    password = request.forms.get('password2')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
run(host='localhost', port=8080)

