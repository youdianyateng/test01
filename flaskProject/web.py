from flask import Flask,render_template,request

app = Flask(__name__)




@app.route("/regist/info", methods=["GET","POST"])
def regist_info ():
    if request.method == "GET":
        return render_template("regist_info.html")
    else:
        user = request.form.get("user")
        pwd = request.form.get("pwd")
        gender = request.form.get("gender")
        hobby = request.form.getlist("gender")
        city = request.form.get("city")
        more = request.form.get("more")
        print(user, pwd, gender, hobby, city, more)

        return "注册成功"

@app.route("/login/info", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:

        print(request.form)
        return"登录成功"





if __name__=='__name__':
    app.run()