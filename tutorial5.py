'''
Cookie: 
Is stored client side (locally in the web browser) and is NOT a secure way to store sensitive information like passwords. It is often used to store things like where a user left on a page, 
or their username so it can be auto-filled in the next time they visit the page. 
It is technically possible for someone to modify cookie data.
Session: 
Is stored server side (on the web server) in a temporary directory. 
It is encrypted information and is a secure way to store information. 
Sessions are often used to store information that should not be seen by the user or should not be tampered with.
'''
from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
	return render_template("index2.html")

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		session.permanent = True
		user = request.form["nm"]
		session["user"] = user
		return redirect(url_for("user"))
	else:
		if "user" in session:
			return redirect(url_for("user"))

		return render_template("login.html")

@app.route("/user")
def user():
	if "user" in session:
		user = session["user"]
		return f"<h1>{user}</h1>"
	else:
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	session.pop("user", None)
	return redirect(url_for("login"))

if __name__ == "__main__":
	app.run(debug=True)