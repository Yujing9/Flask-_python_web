from flask import Flask, app,redirect,url_for,render_template
app = Flask(__name__)
@app.route("/")
def home():
    #must put it into the template folder
    #{{Variable/Statement}}will tell flask to evaluate the statement
    # inside the brackets and render the text equivalent to it.
    return render_template("index.html",content = "testing",x = "4",dic = {"a":2, "b":"hello"})
#Dynamic URLs
@app.route("/<name>")
def user(name):
    return f"hello{name}!"
#Redirects
@app.route("/admin")
def admin():
    return redirect(url_for("user",name = "Admin"))
if __name__ == "__main__":
    app.run()   