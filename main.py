from flask import Flask, request, redirect, render_template
import cgi
import os 



app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods = ['GET'])
def index():
    return render_template('home_page.html')

def is_not_empty(input):
    if input:
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

def not_valid_email(input):
    if "." in input and "@" in input:
        return False
    else:
        return True

@app.route("/", methods=["POST"])
def validate():
    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""
    

    #username logic
    if contains_space(username) or not_correct_length(username):
        username_error = "Not a vaild username"
        username = username
        password = ""
        verify_password = ""

    #password logic
    if contains_space(password) or not_correct_length(password):
        password_error = "Not a vaild password"
        password = ""

    #verify_password logic
    if verify_password != password:
        verify_password_error="Passwords don't match"
        verify_password = ""

    #email logic:
    if is_not_empty(email) and (not_correct_length(email) or contains_space(email) or not_valid_email(email)):
        email_error = "Not a valid email"
        email = email
        password = ""
        verify_password = ""
    

        



    


    if not username_error and not password_error and not verify_password_error and not email_error:
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
        email=email,
        title="user signup")   

@app.route("/welcome")
def valid_info():
    new_user = request.args.get('new_user')
    return render_template('welcome_page.html', name = new_user, title = "welcome")





app.run() 