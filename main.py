from flask import Flask, request, redirect, url_for, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True
#app.config['TRAP_BAD_REQUEST_ERRORS'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def validate():
    print("This is a test")
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    if username == '':
        username_error = 'Please fill in a username'
        email = email
    elif password == '':
        password_error = 'Please fill in a password'
        username = username
        email = email
    elif str.isalpha(password) == False or len(password) < 3 or len(password) > 20:
        password_error = 'Choose a password between 3 and 20 alphabetical characters'
        username = username
        email = email
    elif ' ' in username or len(username) < 3 or len(username) > 20:
        username_error = 'Choose a username between 3 and 20 alphabetical characters'
        email = email
    elif password != verify:
        verify_error = 'The password does not match what is in the verification box'
        username = username
        email = email
    elif email != '' and ('@' not in email or '.' not in email or len(email) < 3 or len(email) > 20):
        email_error = 'Please enter a valid email between 3 and 20 alphanumeric characters'
        username = username
        email = email
    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username = username)
    else:
        return render_template('index.html', username = username, email = email, username_error = username_error, password_error = password_error, verify_error = verify_error, email_error = email_error)

app.run()