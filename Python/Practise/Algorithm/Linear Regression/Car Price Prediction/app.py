#
from flask import Flask,render_template,request
from flask_cors import CORS,cross_origin
import pickle
app=Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def homePage():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
@cross_origin()
def index():
    if request.method=='POST':
        try:
            current_price=float(request.form['current_price'])



if __name__ == '__main__':
     app.run(port=8080)