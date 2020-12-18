from flask import Flask,render_template,request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app=Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def homePage():
    return render_template('index.html')

@app.route('/')