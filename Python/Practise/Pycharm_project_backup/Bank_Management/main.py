from flask import Flask,request,render_template
import json

app=Flask(__name__)

with open('config.json','r') as c:
    params =json.load(c)['params']

@app.route('/',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/welcome',methods=['GET','POST'])
def welcome():
    name="parag naik"
    return render_template('welcome.html',name=name)

app.run(debug=True)