#Blueprints & Using Multiple Python Files
#when you reuse a file name, blueprints will come in handy.
#https://flask.palletsprojects.com/en/2.0.x/blueprints/
#加入__init__.py代表着他是一个蓝图
from flask import Flask
from flask import Flask,render_template
#当我们的second 移动到model文件夹的时候，我们会发现无法导入包,这时候我们需要在前面加入路径，但是slash要用point 代替
from model.second import second
app = Flask(__name__)
#app.register_blueprint(second,url_prefix="")
#当我的“”为blank的时候，意味着，无论什么时候访问，都通过second 访问
app.register_blueprint(second,url_prefix="/admin")
#如果想分主次，就要在“”里面增加路径
@app.route("/")
@app.route("/home")
def test():
    return "<h1>Test</h1>"
if __name__ == "__main__":
    app.run(debug= True)