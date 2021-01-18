from flask import Flask,render_template,request
import random

app=Flask(__name__)

@app.route("/",methods=['GET'])
def homepage():
    return render_template("index.html")

@app.route("/",methods=['POST'])
def generate():
    if request.method=="POST":
        try:
            length=int(request.form['length'])
            s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
            p = "".join(random.sample(s, length))
            msg="This is your password-"
            return render_template("index.html",msg=msg,p=p)
        except Exception as e:
            print("The exception message is-", e)
            return "Something is wrong"
    else:
        return render_template("index.html")

app.run(debug=True)