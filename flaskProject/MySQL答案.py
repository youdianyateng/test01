from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/show/info")
def index():
    return render_template("index.html")
@app.route("/get/news")
def get_news ():
    return render_template("get_news.html")
@app.route("/daan2/news")
def daan2_news ():
    return render_template("daa2.html")