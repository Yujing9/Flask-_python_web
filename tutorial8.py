#Adding, Deleting & Updating Users w/ SQLAlchemy
from os import name
from flask import Flask, redirect, url_for, render_template, request, session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"
#load the configuration of choice 
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  #from document
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)
db = SQLAlchemy(app)
#create the SQLAlchemy object
class users(db.Model):
	_id = db.Column ("id",db.Integer,primary_key = True) #生成数据表，id为unique主键并且自动生成
	name = db.Column(db.String(100))#声明他是字符串
	email = db.Column(db.String(100))#声明他是字符串
	def __init__(self,name,email) -> None:#初始化变量
		self.name = name
		self.email = email
		
@app.route("/")
def home():
	return render_template("index2.html")

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		session.permanent = True
		user = request.form["nm"]
		session["user"] = user
		#Accessing the data in database 
		found_user = users.query.filter_by(name = user).first()
		if found_user:
			session["email"] = found_user.email 
		else:
			usr = users(user,"") #create some users:
			#Adding
			db.session.add(usr)
			#Keeping
			db.session.commit()
		flash("Login successful!")
		return redirect(url_for("user"))
	else:
		if "user" in session:
			flash("Already logged in!")
			return redirect(url_for("user"))
		return render_template("login.html")

@app.route("/user",methods = ["POST","GET"])
def user():
	email = None
	if "user" in session:
		user = session["user"]
		#return f"<h1>{user}</h1>"
		if request.method == "POST":
			email = request.form["email"]
			session["email"] = email
			found_user = users.query.filter_by(name = user).first()
			found_user.email = email
			db.session.commit()
			flash("Email was saved!")
		#return render_template("user.html",user = user )
		else:
			if "email" in session:
				email = session["email"]
		return render_template("user.html",email = email )
	else:
		flash("You are not logged in!")
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	if "user" in session:
		user = session["user"]
		flash(f"You were successfully logged out,{user}","info")
	session.pop("user", None)
	session.pop("email", None)
	#flash('You were successfully logged out')
	return redirect(url_for("login"))
@app.route("/view")
def view():
	return render_template("view.html",values = users.query.all())

if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)