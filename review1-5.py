#review
from flask import Flask,request,session
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from datetime import timedelta
app = Flask(__name__)
#encrypt 
app.secret_key = "hello"
#creating a permanent session,not long time
app.permanent_session_lifetime = timedelta(minutes=5)
#home
@app.route("/")
def home():
    return render_template("index.html")
#user
@app.route("/user")
def user():
    if "user" in session :
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))
#admin
@app.route("/admin")
def admin():
    return redirect(url_for("home"))
#login
@app.route("/login",methods = ["POST","GET"])
def login():
    #judge whether we submit message
    if request.method == "POST":
        # <--- makes the permanent session
        session.permanent = True  
        #get message from form
        user = request.form["nm"]
        #keep information
        session["user"] = user
        return redirect(url_for("user",usr = user))
    else:
        #if we already keep information in the session
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")
#logout
@app.route("/logout")
def logout():
    #session.pop(“key”, What to do if key doesn’t exist).
    session.pop("user",None)
    return redirect(url_for("login"))
    #return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(debug=True)