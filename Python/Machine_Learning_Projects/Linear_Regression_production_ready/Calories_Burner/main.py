from flask import Flask,request,render_template
import pickle

app=Flask(__name__)


@app.route('/',methods=['GET'])
def homepage():
    return render_template("index.html")

@app.route('/predict',methods=['GET','POST'])
def prediction():
    if request.method=='POST':
        try:
            duration=float(request.form['duration'])
            heart_rate=float(request.form['heart_rate'])
            body_temp=float(request.form['body_temp'])

            filename ='Calorie_burner_unscaled.pickle'
            loaded_model=pickle.load(open(filename,'rb'))
            prediction=loaded_model.predict([[duration,heart_rate,body_temp]])
            print('prediction is ',prediction[0])
            return render_template('result.html',prediction=prediction[0],duration=duration)
        except Exception as e:
            print("The exception message is-",e)
            return "Something is wrong"
    else:
        return render_template('index.html')

app.run(debug=True)


