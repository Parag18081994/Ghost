from flask import Flask,render_template,request,Response
import pickle
app=Flask(__name__)

def predict_crop()=


@app.route("/",methods=['GET'])
def index():
    return render_template('Crop_Recommendation.html')


@app.route("/predict",methods=["GET","POST"])
def prediction():
    if request.method=='POST':
        try:
            nitrogen=float(request.form['nitrogen'])
            phosphorus=float(request.form['phosphorus'])
            potassium=float(request.form['potassium'])
            temperature=float(request.form['temperature'])
            humidity=float(request.form['humidity'])
            ph=float(request.form['ph'])
            rainfall=float(request.form['rainfall'])

            filename='modelForPrediction.sav'
            load_model=pickle.load(open(filename,'rb'))
            prediction=load_model.predict([[nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall]])
            print(prediction)
            return render_template('',prediction=prediction)

        except ValueError:
            return Response("value not found")
        except Exception as e:
            print("Exception is ",e)
            return Response(e)
    else:
        return render_template("Crop_Recommendation.html")

if __name__=='__main__':
    app.run(debug=True)


