from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def Hello():
    #return "Hello Flask world!"
    return render_template("index.html")

@app.route("/about")
def hi():
    name="Parag"
    #return "Hello Parag Bhai!!"
    return render_template("about.html",name2=name)

app.run()