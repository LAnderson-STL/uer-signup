from flask import Flask, request, redirect, render_template
import cgi
import os 

#import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/home")
def index():
    return render_template('home_page.html')


#@app.route("/welcome", methods=['POST'])
#def hello():
    #first_name = request.form['first_name']
    #return render_template('hello_greeting.html', name=first_name)

#@app.route('/home')
#def display_signup_form():
    #return render_template('home_page.html.html')

def is_empty(input):
    if input == "":
        return True
    else:
        return False

def not_correct_length(input):
    if not len(input) < 3 and not len(input) > 20:
        return False
    else:
        return True

def contains_space(input):
    if " " in input:
        return True
    else: 
        return False

def valid_email(input):
    if "." in input and "@" in input:
        return True
    else:
        return False

@app.route("/home", methods=["POST"])
def validate():
    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = ["email"]

    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""
    

    #username logic
    if is_empty(username) or contains_space(username) or not_correct_length(username):
        username_error = "Not a vaild username"
        username = ""

    #password logic
    if is_empty(password) or contains_space(password) or not_correct_length(password):
        password_error = "Not a vaild password"
        password = ""

    #verify_password logic
    if verify_password != password:
        verify_password_error="Passwords don't match"

    #email logic:
    if not is_empty(email) and 
        if contains_space(email):
            email_error = "Not a valid email"
            email = ""
        elif not valid_email(email):
            email_error = "Not a valid email"
            email = ""



        



    


    if not username_error and not password_error and not verify_password_error: #and not email_error:
        new_user = username
        return redirect('/welcome?new_user={0}'.format(new_user))
    else:
        return render_template('home_page.html', 
        username_error=username_error, 
        password_error=password_error,
        verify_password_error= verify_password_error,
        email_error=email_error,
        username = username, 
        password=password,
        verify_password=verify_password,
        email=email)   

@app.route("/welcome")
def valid_info():
    new_user = request.args.get('new_user')
    return "<h1>Welcome, {0}!</h1>".format(new_user)





app.run() 