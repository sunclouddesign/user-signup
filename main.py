from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/", methods=['POST'])


def check_valid():
    # look inside the request to figure out what the user typed
    #new_username = request.args.get('username')
    new_username = request.form['username']
    new_pass = request.form['password']
    vnew_pass = request.form['vpassword']
    new_email = request.form['email']
    uname_error = ''
    pass_error = ''
    vpass_error = ''
    email_error = ''

    # if the user typed nothing at all, redirect and tell them the error
    if (not new_username) or (new_username.strip() == ""):
        uname_error = "Error: Username left blank."

    # if the user tries to enter a password that is too short, too long, or contains space
    if len(new_pass) < 3 or len(new_pass) > 20 or (not new_pass) or (new_pass.strip() == ""):
    #if '@' not in new_email or '.' not in new_email or len(new_email) < 3 or len(new_email) > 20:
        pass_error = "Please enter a password between 3 and 20 characters long."
        #return redirect("/?error=" + error)

    if new_pass != vnew_pass or (vnew_pass.strip() == "") or (not vnew_pass):
        vpass_error = "Please verify password by entering password again."
        #return redirect("/?error=" + error)

    if (new_email):
        if '@' not in new_email or '.' not in new_email or len(new_email) < 3 or len(new_email) > 20:
            email_error = "Not a valid email"
            #return redirect("/?error=" + error)

    if not pass_error and not vpass_error and not email_error and not uname_error:
        # If no errors, send user to the welcome page, passing the username
        #return render_template('welcome.html', username=username_escaped)
        #return redirect("/welcome",username=cgi.escape(request.form['username']))
        return redirect("/welcome?username=" + new_username)

    else:
        return render_template('form.html', email_error=email_error,
            uname_error=uname_error,
            vpass_error=vpass_error,
            pass_error=pass_error)

    #return render_template('form.html')        

@app.route("/welcome")
def welcome_user():
    # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
    #username=cgi.escape(request.form['username'], quote=True)
    username = request.args.get("username")
    return render_template('welcome.html',username=username and cgi.escape(username, quote=True))

@app.route("/")
def index():
    #encoded_error = request.args.get("error")
    return render_template('form.html')


app.run()