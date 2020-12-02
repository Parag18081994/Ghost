from flask import Flask,render_template,request,jsonify
import pickle

app=Flask(__name__)

@app.route('/',methods=['GET'])
def homePage():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def index():
    if request.method=='POST':
        try:
            Hours=float(request.form['Hours'])
            filename='finalized_Student_mark_model.pickle'
            loaded_model=pickle.load(open(filename,'rb'))
            prediction=loaded_model.predict([[Hours]])
            print('Prediction is ',prediction)

            return render_template('result.html',prediction=round(prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return('something is wrong')
    else:
        return render_template('index.html')

if  __name__=='__main__':
    app.run(debug=True)
