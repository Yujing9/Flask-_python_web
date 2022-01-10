from flask import Flask, app,redirect,url_for
app = Flask(__name__)
@app.route("/")
def home():
    return "hello"
#Dynamic URLs
@app.route("/<name>")
def user(name):
    return f"hello{name}!"
#Redirects
@app.route("/admin")
def admin():
    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run()