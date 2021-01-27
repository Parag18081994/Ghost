from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def hello():
    return "Hi,I am Parag and fun to learn flask!"

@app.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap.html")

app.run()