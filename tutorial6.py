#flash
#English:Good applications and user interfaces are all about feedback. 
# If the user does not get enough feedback they will probably end up hating the application. 
# Flask provides a really simple way to give feedback to a user with the flashing system. 
# The flashing system basically makes it possible to record a message at the end of a request and access it next request and only next request. 
#中文：flash()函数，它可以用来“闪现”需要提示给用户的消息，比如当用户登录成功后显示“欢迎回来！”。
#在视图函数调用flash()函数，传入消息内容，
# flash（）函数把消息存储在session中，我们需要在模板中使用全局函数get_flashed_messages()获取消息并将它显示出来。
from flask import Flask, redirect, url_for, render_template, request, session,flash
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
		flash("Login successful!")
		return redirect(url_for("user"))
	else:
		if "user" in session:
			flash("Already logged in!")
			return redirect(url_for("user"))
		return render_template("login.html")

@app.route("/user")
def user():
	if "user" in session:
		user = session["user"]
		#return f"<h1>{user}</h1>"
		return render_template("user.html",user = user )
	else:
		flash("You are not logged in!")
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	if "user" in session:
		user = session["user"]
		flash(f"You were successfully logged out,{user}","info")
	session.pop("user", None)
	#flash('You were successfully logged out')
	return redirect(url_for("login"))

if __name__ == "__main__":
	app.run(debug=True)